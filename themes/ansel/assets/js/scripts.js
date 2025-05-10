var bypass_hide = false;

/* Auto-hide elements on scroll-down, show them on scroll-up */
document.addEventListener("DOMContentLoaded", function () {
  el_autohide = document.querySelector('.autohide');

  if (el_autohide) {
    var last_scroll_top = 0;
    window.addEventListener('scroll', function (event) {
      if (bypass_hide) { return; }

      let scroll_top = window.scrollY;
      if (scroll_top < last_scroll_top) {
        document.body.parentNode.classList.remove('move-up');
        el_autohide.classList.remove('scrolled-down');
        el_autohide.classList.add('scrolled-up');
      }
      else {
        document.body.parentNode.classList.add('move-up');
        el_autohide.classList.remove('scrolled-up');
        el_autohide.classList.add('scrolled-down');
      }
      last_scroll_top = scroll_top;
    }, { passive: true });
  }
});

/* Manually force showing */
function force_show() {
  bypass_hide = !(bypass_hide);

  if (bypass_hide) {
    el_autohide = document.querySelector('.autohide');
    sidebars = document.querySelectorAll('.sidebar');

    el_autohide.classList.remove('scrolled-down');
    el_autohide.classList.add('scrolled-up');
    sidebars.forEach((element) => element.classList.remove('move-up'));
    document.body.parentNode.classList.remove('move-up');
  }
}

// Move footnotes to the side margin if screen is wide enough
function y_overlap(A, B) {
  // does A overlap B vertically ?
  return !((A.top > B.bottom && A.bottom > B.bottom) || // A is fully contained below B
           (A.top < B.top && A.bottom < B.top));        // A is fully contained above B
}

class particle {
  // Define each possibly-overlapping element as a particle having
  // a weight, a surface and a center.
  constructor(elem, unmovable, scrollTop, scrollLeft, clientTop, clientLeft) {
    this.width = elem.offsetWidth;
    this.height = elem.offsetHeight;

    var box = elem.getBoundingClientRect();
    var body = document.body;
    var docEl = document.documentElement;

    this.top  = box.top + scrollTop - clientTop;
    this.bottom = this.top + this.height;

    this.left = box.left + scrollLeft - clientLeft;
    this.right = this.top + this.width;

    this.x = this.left + this.width / 2.;
    this.y = this.top + this.height / 2.;

    this.weight = (unmovable) ? Infinity : this.width * this.height;
    this.unmovable = unmovable;

    this.elem = elem;
  }
}


function position_sidenotes()
{
  let startTime = performance.now();

  // Global scrolling coordinates in page
  var body = document.body;
  var docEl = document.documentElement;
  var scrollTop = window.scrollY || docEl.scrollTop || body.scrollTop;
  var scrollLeft = window.scrollX || docEl.scrollLeft || body.scrollLeft;
  var clientTop = docEl.clientTop || body.clientTop || 0;
  var clientLeft = docEl.clientLeft || body.clientLeft || 0;

  var content_body = document.querySelector('#content-body');
  if (!content_body) return;

  // Get only the main page footnotes in case we have footnotes also in slides or figures
  var footnotes_div = document.querySelector('#content-body section > div.footnotes') || document.querySelector('#content-body > div.footnotes');
  if (!footnotes_div) return;
  var footnotes = footnotes_div.querySelectorAll('li');
  if (!footnotes) return;

  const container = new particle(content_body, true,
  scrollTop, scrollLeft, clientTop, clientLeft)

  // Size of a relative em
  var rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
  var vertical_margin = 1.5 * rem;

  // Create the marginnotes nodes by duplicating footnotes nodes
  for (i = 0; i < footnotes.length; i++) {
    var content = footnotes[i];
    var new_node = document.createElement("span");
    new_node.innerHTML = content.innerHTML;
    new_node.role = content.role;
    new_node.id = content.id.replace(/^f/, "s"); // rename fn to sn to keep ids unique
    new_node.classList.add("sidenote");

    var backref = content.querySelector('a.footnote-backref');
    var backref_target = backref.getAttribute("href");

    // Can't use querySelector("#fn:1") because #fn:1 has an invalid :
    // so we need to pass fn:1 to getElementById instead.
    var backref_id = backref_target.replace(/^\#/, '');
    var ref = document.getElementById(backref_id);
    var number = backref_target.replace(/^\#fnref:/, '');
    new_node.innerHTML = "<span class='sidenote-number'>" + number + ".</span>" + new_node.innerHTML;

    var paragraph = ref.parentNode;
    paragraph.style.position = "relative";

    var left = paragraph.offsetLeft + paragraph.offsetWidth;
    var max_width = content_body.offsetLeft + content_body.offsetWidth - left;

    if (max_width > 149) {
      // Insert the sidenote only if we have enough space
      new_node.style.width = max_width + "px";
      new_node.style.left = paragraph.offsetWidth + "px";
      paragraph.append(new_node);
      new_node.style.top = ref.offsetTop + "px";
    }
  }

  // Manage sizes and overlapping of notes
  var sidenotes = content_body.querySelectorAll('span.sidenote, h2, img, figure, blockquote.floating-quote, div.annotation, div.footnotes, div.highlight, .full-width, .mermaid, div.meta');
  var particles = [];
  for (i = 0; i < sidenotes.length; i++) {
    particles.push(new particle(sidenotes[i], (sidenotes[i].tagName != "SPAN"),
      scrollTop, scrollLeft, clientTop, clientLeft));
    // console.log(sidenotes[i]);
  }

  // Build the matrix of vertical overlapping and the vector of unmovable items
  // Note : each element overlaps over itself.
  var matrix = [];
  for (i = 0; i < particles.length; i++) {
    matrix[i] = [];
    // Note to non-JS-devs : `+` on boolean vars casts them to int (ugly idiom)
    for (j = 0; j < particles.length; j++) {
      matrix[i][j] = + y_overlap(particles[i], particles[j]);
    }
  }

  // console.log(matrix);

  // Split the page into sub-problems for each set of overlapping footnotes :
  // Each row of the matrix is a sub-problem.
  for (i = 0; i < particles.length; i++) {
    // Find the indices of the overlapping elements if any
    var indices = [];
    for (j = 0; j < particles.length; j++)
      if (matrix[i][j] == 1)
        indices.push(j);

    if (indices.length > 1) {
      // We have overlapping.

      // Find the fences, aka the closest previous and next unmovable elements
      // Defaults to container bounding box if no fence is found.
      // We assume here that fences are distributed across the current element.
      // If they are not, we are screwed, but the logic of checking overlapping
      // between current element and every other element seems to prevent that case.
      var previous_bound = -1;
      for (k = indices[0]; k >= 0; k--)
        if (particles[k].unmovable) {
          previous_bound = k;
          break;
        }

      var next_bound = -1;
      for (k = indices[indices.length - 1]; k < particles.length; k++)
        if (particles[k].unmovable) {
          next_bound = k;
          break;
        }

      // console.log("bounds", previous_bound, next_bound);

      // Get the min/max vertical coordinates, linked to the fences
      var y_min = (previous_bound > -1 ) ? particles[previous_bound].bottom : container.top;
      var y_max = (next_bound > - 1) ? particles[next_bound].top : container.bottom;

      // console.log("coord", y_min, y_max);

      // Check that we have at least enough vertical space to fit all elements back-to-back
      // in-between fences
      var total_height = 2 * vertical_margin;
      for (k = previous_bound + 1; k < next_bound; k++)
        total_height += particles[k].height + rem;
      total_height -= rem;

      // console.log("total height", total_height);

      if (total_height > y_max - y_min) {
        // we simply can't fit all footnotes between fences. Hide them all then.
        for (k = previous_bound + 1; k < next_bound; k++) {
          if (!particles[k].unmovable)
            particles[k].elem.style.display = "none";
        }
      }
      else {
        // We can fit all footnotes there, at least between fences.
        // Now, check if we can fit them between first overlapping elem and the next fence.
        // That keeps the first footnote on the floating line of its reference.
        // Works only if the first overlapping element is not a fence
        var cumulative_height = y_min;

        if (total_height <= y_max - particles[previous_bound + 1].top && previous_bound != indices[0])
          cumulative_height = particles[previous_bound + 1].top;
        else {
          // If the first overlapping element is a fence, give it some extra vertical margin
          cumulative_height += vertical_margin;
        }

        // Now, reposition every element between bounds. Even the non-overlapping ones to be safe.
        // TODO: reposition only overlapping elements and check if the new position overlap
        // previously-good elements sitting between bounds.
        for (k = previous_bound + 1; k < next_bound; k++) {
          if (particles[k].unmovable) continue;

          var current_particle = particles[k].elem;

          // Get the global position of the parent in the page
          var parent = current_particle.parentNode;
          var box = parent.getBoundingClientRect();
          const parent_top = box.top + scrollTop - clientTop;

          // Assign the new position to the element and update data
          var new_top = cumulative_height - parent_top;
          current_particle.style.top = new_top + "px";
          particles[k].top = cumulative_height;
          particles[k].bottom = particles[k].top + particles[k].height;

          // Update the cumulative height
          cumulative_height += particles[k].height + rem;

          // Update the overlapping matrix for this column for the next rows.
          // No need to solve it again.
          for (j = k; j < particles.length; j++)
            matrix[j][k] = 0;
        }
      }
    }
  }

  let endTime = performance.now();
  let timeElapsed = endTime - startTime;
  console.log("The footnote code took " + timeElapsed + ' milliseconds');
}

function remove_sidenotes() {
  var sidenotes = document.querySelectorAll('span.sidenote');
  if (sidenotes.length == 0) return;

  for (i = 0; i < sidenotes.length; i++) {
    sidenotes[i].parentNode.removeChild(sidenotes[i]);
  }
}

window.addEventListener('DOMContentLoaded', () => {
  position_sidenotes();
});

window.addEventListener('resize', () => {
  remove_sidenotes();
  position_sidenotes();
});

/* Progress bar for posts */
const numSteps = 20.0;

function buildThresholdList() {
  let thresholds = [0];

  for (let i = 1.0; i <= numSteps; i++) {
    let ratio = i / numSteps;
    thresholds.push(ratio);
  }

  return thresholds;
}

function handleIntersect(entries, observer) {
  console.log("fired");
  entries.forEach((entry) => {
    console.log(entry);
    console.log(entry.intersectionRatio);
  });
}

function set_progress_bar()
{
  let boxElement = document.getElementById("content-body");
  const rect = boxElement.getBoundingClientRect();
  var pos = Math.max(Math.min(-rect.y + window.innerHeight, rect.height), 0.) / rect.height;
  document.getElementById("post-progress-fg").style.width = pos * 100. + "%";
}

window.addEventListener(
  "DOMContentLoaded",
  function () {
    let boxElement = document.getElementById("content-body");

    if (boxElement) {
      // Create progress bar markup
      let progress_bar = document.createElement("div");
      progress_bar.innerHTML = `<div id="post-progress-fg"></div>`;
      progress_bar.id = "post-progress-bg";
      document.body.appendChild(progress_bar);

      set_progress_bar();
      window.addEventListener("scroll", set_progress_bar, true);

      /* Tracks only for thresholds = 0 or 1. Debug...
      let observer = new IntersectionObserver(handleIntersect, { threshold: buildThresholdList(), root: null, rootMargin: "0px" });
      observer.observe(boxElement);
      console.log(observer);
      */
    }

  },
  false,
);

/*
 * Client-side comparison slider for images.
 * Loosely based on https://codepen.io/Coding_Journey/pen/QWdQraQ and
 * https://www.w3schools.com/howto/howto_js_image_comparison.asp.
 *
 * Copyright © 2022 - Aurélien Pierre.
 */

function set_fifty_fifty_sizes(width, height, parent) {
  var slider = parent.getElementsByClassName("img-comp-container")[0];
  var over = parent.getElementsByClassName("img-comp-over")[0];
  var over_image = over.getElementsByTagName("img")[0];
  var under = parent.getElementsByClassName("img-comp-under")[0];
  var under_image = under.getElementsByTagName("img")[0];

  slider.style.height = height + "px";
  over_image.style.height = height + "px";
  under_image.style.height = height + "px";
  over.style.height = height + "px";
  under.style.height = height + "px";

  slider.style.width = width + "px";
  over_image.style.width = width + "px";
  under_image.style.width = width + "px";
  over.style.width = (width / 2) + "px";
  under.style.width = width + "px";
}

function compute_bounding_box(slider, image_ratio, full_width=true) {
  // Compute the bounding box of the slider that will fit it entirely
  // taking into account its image ratio and container sizes
  // Set full_width to false for lightbox mode, where we need to fit
  // the whole image in the viewport. Otherwise, the height will be adapted
  // flexibly depending on width, even if it can't be displayed entirely in viewport
  var cs = getComputedStyle(slider.parentNode);
  var paddingX = parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight);
  var paddingY = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom);
  var borderX = parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth);
  var borderY = parseFloat(cs.borderTopWidth) + parseFloat(cs.borderBottomWidth);

  max_width = slider.parentNode.offsetWidth - paddingX - borderX;
  max_height = slider.parentNode.offsetHeight - paddingY - borderY;
  screen_ratio = max_width / max_height;

  if (full_width) {
    width = max_width;
    height = max_width / image_ratio;
  }
  else {
    if( image_ratio < screen_ratio)
    {
      height = max_height;
      width = max_height * image_ratio;
    }
    else {
      width = max_width;
      height = max_width / image_ratio;
    }
  }

  return [width, height];
}

function set_heights(slider, full_width) {
  /* Sliders use 100% of column width and auto-adjust their height.
  We need to anchor the height of everything to the one of the smallest image */
  var over = slider.getElementsByClassName("img-comp-over")[0];
  var over_image = over.getElementsByTagName("img")[0];
  var under = slider.getElementsByClassName("img-comp-under")[0];
  var under_image = under.getElementsByTagName("img")[0];

  /* Set all containers heights to the min of images */
  height = Math.min(under_image.offsetHeight, over_image.offsetHeight);
  width = Math.min(under_image.offsetWidth, over_image.offsetWidth);
  sizes = compute_bounding_box(slider.parentNode, width / height, full_width);
  set_fifty_fifty_sizes(sizes[0], sizes[1], slider.parentNode);

  return sizes;
}

function reset_cursor(slider, sizes) {
  cursor = slider.getElementsByClassName("comp-cursor")[0];
  cursor.style.top = (sizes[1] / 2) - (cursor.offsetHeight / 2) + "px";
  cursor.style.left = (sizes[0] / 2) - (cursor.offsetWidth / 2) + "px";
}

/* Dynamically resize images with regard to the lightbox bounding box
* @param: lightbox container
* @param : in_wrappers : original wrappers where image ratios are computed
* @param : out_wrappers : destination wrappers where image sizes are applied
* They can be the same.
*/
function resize_images(lightbox, in_wrappers, out_wrappers) {
  console.assert(in_wrappers.length == out_wrappers.length);

  var height = 0, width = 0;

  for (j = 0; j < in_wrappers.length; j++) {
    // Step 1: measure max sizes in original wrapper
    var images = in_wrappers[j].getElementsByTagName("img");

    for (i = 0; i < images.length; i++) {
      height = Math.max(height, images[i].naturalHeight);
      width = Math.max(width, images[i].naturalWidth);
    }
  }
  sizes = compute_bounding_box(document.getElementById("lightbox-slider"), width / height, false);

  for (j = 0; j < out_wrappers.length; j++) {
    // Step 2: apply the size to the destination wrapper
    images = out_wrappers[j].getElementsByTagName("img");
    for (i = 0; i < images.length; i++) {
      images[i].style.height = sizes[1] + "px";
      images[i].style.width = sizes[0] + "px";
    }

    // Apply new sizes to container too
    var container = out_wrappers[j].getElementsByClassName("img-container")[0];
    container.style.height = sizes[1] + "px";
    container.style.width = sizes[0] + "px";
  }
}

window.addEventListener('resize', function () {
  // Handle comparisons
  x = document.getElementsByClassName("img-comp-container");

  for (i = 0; i < x.length; i++) {
    full_width = x[i].parentNode.id != "lightbox-slider";
    sizes = set_heights(x[i], full_width);
    reset_cursor(x[i], sizes);
  }

  // Handle regular lightboxes
  box = document.getElementById("lightbox");
  if (box) {
    // Lightbox mode
    resize_images(box, box.getElementsByClassName("img-wrapper"),
      box.getElementsByClassName("img-wrapper"));
  }
})

function initComparisons(id=false) {
  var x, i;
  /* Find all elements with an "overlay" class and add the events */
  if (!id) {
    // Inline sliders
    x = document.getElementsByClassName("img-comp-container");
    for (i = 0; i < x.length; i++) {
      set_heights(x[i], true);
      compareImages(x[i]);
    }
  }
  else {
    // lightbox slider
    container = document.getElementById(id);
    x = container.getElementsByClassName("img-comp-container")[0];
    set_heights(x, false);
    compareImages(x);
  }

  function compareImages(slider) {
    var cursor, clicked = 0;

    var over = slider.getElementsByClassName("img-comp-over")[0];
    var under = slider.getElementsByClassName("img-comp-under")[0];

    /* Create cursor */
    cursor = document.createElement("DIV");
    cursor.setAttribute("class", "comp-cursor");
    cursor.innerHTML = "<div class='comp-cursor-line'></div><div class='comp-cursor-button'><i class='fas fa-chevron-left'></i><i class='fas fa-chevron-right'></i></div><div class='comp-cursor-line'></div>";

    /* Insert slider */
    over.parentElement.insertBefore(cursor, over);
    /* Position the slider in the middle: */
    cursor.style.top = (height / 2) - (cursor.offsetHeight / 2) + "px";
    cursor.style.left = (over.offsetWidth) - (cursor.offsetWidth / 2) + "px";

    /* Execute a function when the mouse button is pressed: */
    cursor.addEventListener("mousedown", slideReady);
    /* And another function when the mouse button is released: */
    window.addEventListener("mouseup", slideFinish);
    /* Or touched (for touch screens: */
    cursor.addEventListener("touchstart", slideReady);
     /* And released (for touch screens: */
    window.addEventListener("touchend", slideFinish);

    function slideReady(e) {
      /* Prevent any other actions that may occur when moving over the image: */
      e.preventDefault();
      /* The slider is now clicked and ready to move: */
      clicked = 1;
      /* Execute a function when the slider is moved: */
      window.addEventListener("mousemove", slideMove);
      window.addEventListener("touchmove", slideMove);
    }

    function slideFinish() {
      /* The slider is no longer clicked: */
      clicked = 0;
    }

    function slideMove(e) {
      var pos;
      /* If the slider is no longer clicked, exit this function: */
      if (clicked == 0) return false;
      /* Get the cursor's x position: */
      pos = getCursorPos(e)
      /* Prevent the slider from being positioned outside the image: */
      if (pos < 0) pos = 0;
      if (pos > width) pos = width;
      /* Execute a function that will resize the overlay image according to the cursor: */
      slide(pos);
    }

    function getCursorPos(e) {
      var a, x = 0;
      e = (e.changedTouches) ? e.changedTouches[0] : e;
      /* Get the x positions of the image: */
      a = slider.getBoundingClientRect();
      /* Calculate the cursor's x coordinate, relative to the image: */
      x = e.pageX - a.left;
      /* Consider any page scrolling: */
      x = x - window.scrollX;
      return x;
    }

    function slide(x) {
      /* Resize the image: */
      over.style.width = x + "px";
      /* Position the slider: */
      cursor.style.left = over.offsetWidth - (cursor.offsetWidth / 2) + "px";
    }
  }
}


function lightbox(id) {
  // If we already have a lightbox, close it
  box = document.getElementById("lightbox");
  if (box) {
    // Restore Plotly ID if any
    var plotly_graph = box.getElementsByClassName("plotly-graph-div");
    var plotly_original = document.getElementById("plotly-original");
    if(plotly_graph && plotly_original)
      plotly_original.id = plotly_graph[0].id;

    // Remove lightbox node
    box.parentNode.removeChild(box);
    document.body.parentNode.style.overflowY = "scroll";
    return;
  }

  // Clone the current figure content
  const template = document.getElementById(id);
  const clone = template.cloneNode(true);
  clone.id = "lightbox-slider"

  // Set responsive sizes of images to 100vw
  var images = clone.getElementsByTagName("img");
  for (i = 0; i < images.length; i++)
    images[i].sizes = "100vw";

  // Remove the current slider cursor
  if (template.classList.contains("img-comp-wrapper"))
  {
    const elements = clone.getElementsByClassName("comp-cursor");
    while (elements.length > 0)
      elements[0].parentNode.removeChild(elements[0]);
  }

  // Change the button icon for a cross
  const button = clone.getElementsByClassName("open-lightbox-icon")[0];
  button.classList.remove('fa-expand-alt');
  button.classList.add("fa-times");

  // Add the slider in an overlay
  const lightbox = document.createElement("div");
  var lightbox_button = clone.getElementsByClassName("open-lightbox-button")[0];
  if (lightbox_button) lightbox.appendChild(lightbox_button);

  var link_button = clone.getElementsByClassName("open-link-button")[0];
  if (link_button) lightbox.appendChild(link_button);

  lightbox.id = "lightbox";
  lightbox.appendChild(clone);
  document.body.appendChild(lightbox);

  if (template.classList.contains("img-comp-wrapper")) {
    // Re-init a new slider
    initComparisons("lightbox");
  }
  else if (template.classList.contains("img-wrapper")) {
    // Resize regular figure.
    resize_images(lightbox, [template], // template IS the input .img-wrapper
      lightbox.getElementsByClassName("img-wrapper"));
  }
  else {
    var plotly_div = lightbox.getElementsByClassName("plotly-graph-div");
    if (plotly_div) {
      // Re-create a Plotly graph from scratch, loading HTML
      var plotly_html = template.dataset.src;
      var plotly_id = plotly_div[0].id;
      document.getElementById(plotly_id).id = "plotly-original";

      // Resize vertically to full-height minus margins
      var rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
      plotly_div[0].style.height = (lightbox.offsetHeight - 2. * rem) + "px";

      // Replace rendered HTML by source
      var container = lightbox.getElementsByClassName("include-container")[0];
      fetch(plotly_html)
        .then(response => response.text())
        .then(html => {
          // Run scripts to render Plotly
          var input = document.createElement("html");
          input.innerHTML = html;
          var array = input.getElementsByTagName('script');
          for (i = 0; i < array.length; i++) eval(array[i].innerHTML);
        });
    }
  }

  document.body.parentNode.style.overflowY = "hidden";
}

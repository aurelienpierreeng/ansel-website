/*
 * Client-side comparison slider for images.
 * Loosely based on https://codepen.io/Coding_Journey/pen/QWdQraQ and
 * https://www.w3schools.com/howto/howto_js_image_comparison.asp.
 *
 * Copyright © 2022 - Aurélien Pierre.
 */

function initComparisons() {
  var x, i;
  /* Find all elements with an "overlay" class and add the events */
  x = document.getElementsByClassName("img-comp-container");
  for (i = 0; i < x.length; i++) {
    var height, width;
    set_heights(x[i]);
    compareImages(x[i]);
  }

  // Run feather icons for chevrons
  feather.replace({ 'stroke-width': 3, 'color': '#fff' });

  function set_heights(slider) {
    /* Sliders use 100% of column width and auto-adjust their height.
    We need to anchor the height of everything to the one of the smallest image */
    var over = slider.getElementsByClassName("img-comp-over")[0];
    var over_image = over.getElementsByTagName("img")[0];

    var under = slider.getElementsByClassName("img-comp-under")[0];
    var under_image = under.getElementsByTagName("img")[0];

    /* Set all containers heights to the min of images */
    height = Math.min(under_image.offsetHeight, over_image.offsetHeight);
    width = Math.min(under_image.offsetWidth, over_image.offsetWidth);

    slider.style.height = height + "px";
    over_image.style.height = height + "px";
    under_image.style.height = height + "px";
    over.style.height = height + "px";
    under.style.height = height + "px";

    /* The overlay is inited at half the slider width size. We can't do it in CSS
    if we want the image ratio to be preserved at flexible width. */
    over.style.width = (width / 2) + "px";
    over_image.style.width = width + "px";
    under_image.style.width = width + "px";
  }

  function compareImages(slider) {
    var cursor, clicked = 0;

    var over = slider.getElementsByClassName("img-comp-over")[0];
    var under = slider.getElementsByClassName("img-comp-under")[0];

    /* Create cursor */
    cursor = document.createElement("DIV");
    cursor.setAttribute("class", "comp-cursor");
    cursor.innerHTML = "<div class='comp-cursor-line'></div><div class='comp-cursor-button'><i data-feather='chevron-left'></i><i data-feather='chevron-right'></i></div><div class='comp-cursor-line'>";

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
      x = x - window.pageXOffset;
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

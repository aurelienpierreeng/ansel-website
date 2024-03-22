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

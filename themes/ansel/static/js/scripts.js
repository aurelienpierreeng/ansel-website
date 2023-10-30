// Make TOC nav links active or not
// Code adapted from https://www.bram.us/2020/01/10/smooth-scrolling-sticky-scrollspy-navigation/
window.addEventListener('DOMContentLoaded', () => {

  const observer = new IntersectionObserver(entries =>
  {
    entries.forEach(entry =>
    {
      const id = entry.target.getAttribute('id');
      if (entry.intersectionRatio > 0)
        document.querySelectorAll('aside nav li a').forEach(section => { section.classList.remove('active'); });
      else {
        var element = document.querySelector(`nav li a[href="#${id}"]`);
        if (element)
          element.parentElement.classList.remove('active');
      }
    })
  });

	// Track all titles that have an `id` applied
  document.querySelectorAll('h2[id]').forEach((section) => {
		observer.observe(section);
  });
  document.querySelectorAll('h3[id]').forEach((section) => {
		observer.observe(section);
	});

});


/* Auto-hide elements on scroll-down, show them on scroll-up */
document.addEventListener("DOMContentLoaded", function(){

  el_autohide = document.querySelector('.autohide');

  if(el_autohide){
    var last_scroll_top = 0;
    window.addEventListener('scroll', function() {
          let scroll_top = window.scrollY;
         if(scroll_top < last_scroll_top) {
              el_autohide.classList.remove('scrolled-down');
              el_autohide.classList.add('scrolled-up');
          }
          else {
              el_autohide.classList.remove('scrolled-up');
              el_autohide.classList.add('scrolled-down');
          }
          last_scroll_top = scroll_top;
    });
  }
});

// Make TOC nav links active or not
// Code adapted from https://www.bram.us/2020/01/10/smooth-scrolling-sticky-scrollspy-navigation/
window.addEventListener('DOMContentLoaded', () => {

	const observer = new IntersectionObserver(entries => {
		entries.forEach(entry => {
			const id = entry.target.getAttribute('id');
      if (entry.intersectionRatio > 0) {
        document.querySelectorAll('aside nav li').forEach((section) => {
          section.classList.remove('active');
        });
        document.querySelector(`nav li a[href="#${id}"]`).parentElement.classList.add('active');
      }
		});
	});

	// Track all titles that have an `id` applied
  document.querySelectorAll('h2[id]').forEach((section) => {
		observer.observe(section);
  });
  document.querySelectorAll('h3[id]').forEach((section) => {
		observer.observe(section);
	});

});

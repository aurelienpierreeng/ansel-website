// Make TOC nav links active or not
// Code from https://ma.ttias.be/adding-a-sticky-table-of-contents-in-hugo-to-posts/#adding-a-table-of-contents-in-hugo
function clearActiveStatesInTableOfContents() {
  document.querySelectorAll('aside nav li').forEach((section) => {
      section.classList.remove('active');
  });
}

// Code adapted from https://www.bram.us/2020/01/10/smooth-scrolling-sticky-scrollspy-navigation/
window.addEventListener('DOMContentLoaded', () => {

	const observer = new IntersectionObserver(entries => {
		entries.forEach(entry => {
			const id = entry.target.getAttribute('id');
      if (entry.intersectionRatio > 0) {
        clearActiveStatesInTableOfContents();
        document.querySelector(`nav li a[href="#${id}"]`).parentElement.classList.add('active');
			} else {
				document.querySelector(`nav li a[href="#${id}"]`).parentElement.classList.remove('active');
			}
		});
	});

	// Track all titles that have an `id` applied
	document.querySelectorAll('h1[id]').forEach((section) => {
		observer.observe(section);
  });
  document.querySelectorAll('h2[id]').forEach((section) => {
		observer.observe(section);
  });
  document.querySelectorAll('h3[id]').forEach((section) => {
		observer.observe(section);
	});

});

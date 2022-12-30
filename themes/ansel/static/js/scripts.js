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

// Create cookie to get the Browser Language
const userLang = navigator.language || navigator.userLanguage;
console.log(userLang);
document.cookie = `nf_lang = ${userLang}`;

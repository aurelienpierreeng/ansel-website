var fuse = "";
var fuse_inited = false;

function create_fuse(db_json) {
  fuseOptions = {
    shouldSort: true,
    includeScore: true,
    minMatchCharLength: 4,
    threshold: 0.,
    ignoreLocation: true,
    keys: [
      { name: "title", weight: 0.8 },
      { name: "summary", weight: 0.6 },
      { name: "contents", weight: 0.5 },
      { name: "permalink", weight: 0.8 },
      { name: "keywords", weight: 0.8 },
    ]
  };

  fuse = new Fuse(db_json, fuseOptions);
  fuse_inited = true;
}

function loadJSON(path) {
  // Load the index.json file from the relevant language and
  // feed it to Fuse search object
  // This is done once for each page load.
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if ((xhr.readyState === 4) && (xhr.status === 200)) {
      create_fuse(JSON.parse(xhr.responseText));
    }
  };
  xhr.open('GET', path, true);
  xhr.send();
}

function truncate(str, n){
  return (str.length > n) ? str.slice(0, n-1) + '&hellip;' : str;
};

function display_result(elem) {
  // Get the HTML template and populate it, then add to the HTML container
  const tbody = document.querySelector("#search-results");
  const template = document.querySelector('#search-result-template');
  const clone = template.content.cloneNode(true);

  title = clone.querySelector("h6")
  title.innerHTML = title.innerHTML.replace("(title)", elem.item.title);
  title.innerHTML = title.innerHTML.replace("(url)", elem.item.permalink);
  title.innerHTML = title.innerHTML.replace("(score)", ((1. - elem.score) * 100.).toFixed(0) + " %");

  summary = clone.querySelector("p");
  summary.innerHTML = summary.innerHTML.replace("(summary)", truncate(elem.item.summary, 140));
  summary.innerHTML = summary.innerHTML.replace("(section)", elem.item.section);

  tbody.appendChild(clone);
}

function no_result(message) {
  // Display a "no result found"
  const tbody = document.querySelector("#search-results");
  const clone = document.createElement("div");
  clone.innerHTML = "<p>" + message + "</p>";
  tbody.appendChild(clone);
}

function search_results() {
  // Empty the HTML result list
  tbody = document.querySelector("#search-results");
  tbody.innerHTML = "";

  if (fuse_inited) {
    pattern = document.getElementById("search-query").value;
    console.log(pattern);
    result = fuse.search(pattern);
    console.log(result);

    if (result.length > 0) {
      for (i = 0; i < result.length; i++) {
        display_result(result[i]);
      }
    } else {
      no_result("Sorry, no result found. Try again with different keywords.");
    }
  }
  else {
    no_result("Sorry, the fuse.js library did not load and research is not available. Try to reload the page.");
  }
}

function search_results_from_keyboard() {
  if(event.key === 'Enter') {
    search_results();
  }
}

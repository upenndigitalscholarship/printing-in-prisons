window.onload = function() {

let page = document.getElementById("collection-title").innerText;


let categories = [{
    title: 'Baseball',
    tag: baseball
  },
  {
    title: 'For Sale at Eastern State',
    tag: for sale
  },
  {
    title: 'Poetry',
    tag: poetry
  },
]

let options = {
  valueNames: [ 'name', 'born' ],
  item: '<li><h3 class="name"></h3><p class="born"></p></li>'
};

let values = [{
    name: 'Jonny Strömberg',
    born: 1986
  },
  {
    name: 'Jonas Arnklint',
    born: 1985
  },
  {
    name: 'Martina Elm',
    born: 1986
}];

let articleList = new List('articles', options, values);

console.log(page)
}
window.onload = function() {

let options = {
  valueNames: [ 'table-title', 'table-author','table-year' ],
};

let articleList = new List('articles', options);

console.log(articleList);
}
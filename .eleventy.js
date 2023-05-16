module.exports = function(eleventyConfig) {
    // Output directory: _site
  
    // Copy `assets/` to `_site/assets`
    eleventyConfig.addPassthroughCopy("assets");
    
  // Get only content that matches a tag
eleventyConfig.addCollection("gossipAdviceJokes", function (collection) {
  // return collection.getAll().filter((item) => item.data.tags == "joke" || item.data.tags == "gossip" || item.data.tags == "advice" || item.data.tags == "jokes");
  let gossip = collection.getFilteredByTag("gossip");
  let joke = collection.getFilteredByTag("joke");
  let jokes = collection.getFilteredByTag("jokes");
  let advice = collection.getFilteredByTag("advice");
  let fullCollection = gossip.concat(joke,jokes,advice);
  //return fullCollection;
      return fullCollection.filter( (item, index) =>
        fullCollection.indexOf(item) == index

    )

});

    // Copy `css/fonts/` to `_site/css/fonts`
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("css/fonts");
  
    // Copy any .jpg file to `_site`, via Glob pattern
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("umpire/*.jpg");
  };
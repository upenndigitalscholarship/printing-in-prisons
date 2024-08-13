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

eleventyConfig.addFilter("dateOnly", function (dateVal, locale = "en-us") {
  var theDate = new Date(dateVal);
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  return theDate.toLocaleDateString(locale, options);
});

	// Return all the tags used in a collection
	eleventyConfig.addFilter("getAllTags", collection => {
		let tagSet = new Set();
		for(let item of collection) {
			(item.data.tags || []).forEach(tag => tagSet.add(tag));
		}
		return Array.from(tagSet);
	});

	eleventyConfig.addFilter("filterTagList", function filterTagList(tags) {
		return (tags || []).filter(tag => ["all", "nav", "post", "posts"].indexOf(tag) === -1);
	});

    // Copy `css/fonts/` to `_site/css/fonts`
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("css/fonts");
  
    // Copy any .jpg file to `_site`, via Glob pattern
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("umpire/*.jpg");
  };

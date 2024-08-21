const { parse } = require("csv-parse/sync");

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

  eleventyConfig.addDataExtension("csv", (contents) => {
    const records = parse(contents, {
      columns: true,
      skip_empty_lines: true,
      relax_column_count: true,
      delimiter: ",",
      trim: true,
    });
    return records;
  });

    // Copy `css/fonts/` to `_site/css/fonts`
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("css/fonts");
  
    // Copy any .jpg file to `_site`, via Glob pattern
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("umpire/*.jpg");
  };


  // for csvs, do I want a 1-to-1 connection between csv file and a collection, custom template
  // or a general csv loader that can be used in any template? Like a general template that is flexible regardless 
  // of the CSV fields/data. Use position rather than header? require header?
  // try making an agnostic data template, see how that goes. 
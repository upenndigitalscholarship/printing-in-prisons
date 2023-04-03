module.exports = function(eleventyConfig) {
    // Output directory: _site
  
    // Copy `assets/` to `_site/assets`
    eleventyConfig.addPassthroughCopy("assets");

    
    // Copy `css/fonts/` to `_site/css/fonts`
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("css/fonts");
  
    // Copy any .jpg file to `_site`, via Glob pattern
    // Keeps the same directory structure.
    //eleventyConfig.addPassthroughCopy("umpire/*.jpg");
  };
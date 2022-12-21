### Converting Pages to Items 

Each page of the newspapers was scanned and turned into an image.  Each page was then OCR’d using Tesseract. Within each page, there are individual articles, sections, and pieces.  This workflow aims to split the page-level texts into item-level texts.  

1. The page-level texts can be found here in the echo and umpire folders: https://github.com/upenndigitalscholarship/printing-in-prisons
2. The page images can be found here: https://github.com/upenndigitalscholarship/printing-in-prisons/tree/main/assets/img
3. Begin by selecting an image to work on (we’ll use this one as an example) <img src="https://github.com/upenndigitalscholarship/printing-in-prisons/blob/main/assets/img/Echo-Fall-1966-Page-03.jpg"/>
4. It helps to take a glance at the whole page to make sense of what’s going on and what the relevant parts will be. There’s a title, “The Superintendent Speaks”, an author Joseph R. Brierley, and three columns of text. This is page 3. I can check on page 2 and 4 to confirm that the article starts and ends on this page.
5. Compare that with the OCR’d version of the page here: https://github.com/upenndigitalscholarship/printing-in-prisons/blob/main/echo/1966/Echo-Fall-1966-Page-03.md
#### Create an item file with metadata
6. Let’s create an item for this text. For this example, I will assume that you are working directly in GitHub, but the same process can be done with VSCode or other code editors.  This is from Echo Fall 1966, so we’ll create an item in the [/main/echo/1966/items](https://github.com/upenndigitalscholarship/printing-in-prisons/tree/main/echo/1966/items) folder (create the folder if needed). For the filename, let’s use 1.md (or 2.md if that already exists). In GitHub open the folder, then click on “add file” > “create new file”.  
![](https://docs.github.com/assets/cb-26723/images/help/repository/create_new_file.png)  

You can enter the filename where it says “Name your file…” Content can be added where it says “Edit new file.”  

![](https://github.blog/wp-content/uploads/2012/12/new-file-editor.png?resize=964%2C419)

7. This is a markdown file, so we can add an initial section with metadata (also called frontmatter).  Simply add a section at the top of the page opened with three dashes and closed with three dashes:
```md
---
title: The Superintendent Speaks
author: Joseph R. Brierley 
newspaper: Eastern Echo
year: 1966
issue: Fall
page: 3
tags:
  - 10th Anniverary
  - Grumpy man in tie
layout: item
---
```
8. Next we can add fields for title, author, newspaper, year, issue, and page (if there's more than one page, give the start and end pages: 1-4).
9. It’s also possible to add filter tags. Add anything you think describes this item as a kind of entry. For example, the warden notes that it’s the 10th Anniversary of the Eastern Echo. We could add a tag for that. Each tag should be on its own line, indented two spaces, then a hyphen, then one space, then the tag. 
10. Finally, add `layout: item` (this determines how the item will be displayed on the website).
11. With the frontmatter complete, we can now paste the text into the file below the three dashes `---`. 

#### Item-level text 
12. The text in this file should include the item's full text from beginning to end. Keep in mind that this may begin or end on different pages.
13. The text will probably include OCR errors. Feel free to make corrections, but the main goal of this step is to create item-level files for the various article in the paper. 
14. When your metadata and text are ready, click on the green "Commit changes" button at the bottom of the screen. You can alway come back to edit the file by clicking on the pencil icon in the upper right-hand corner.  

For the example page, here's what I ended up with (note that there's much more OCR correction to be done): https://github.com/upenndigitalscholarship/printing-in-prisons/blob/main/echo/1966/items/1.md

import os
from glob import glob
import frontmatter

# specify the directory to scan for markdown files
directory_path = '.'

# use glob library to find all markdown files in directory and subdirectories
md_files = [f for f in glob(os.path.join(directory_path, '**/*.md'), recursive=True)]

# loop through each file found
for file in md_files:
    if not 'node_modules' in file:  
        # read the contents of the file
        with open(file, 'r') as f:
            content = f.read()

        # parse the frontmatter using frontmatter library
        post = frontmatter.loads(content)

        # check if page field exists in the frontmatter
        if not 'layout' in post.keys():
            # rename page field to pageNum
            
            print(f"{file}")
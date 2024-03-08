import os
from glob import glob
import frontmatter

# specify the directory to scan for markdown files
directory_path = '.'

# use glob library to find all markdown files in directory and subdirectories
md_files = [f for f in glob(os.path.join(directory_path, '**/*.md'), recursive=True)]

# loop through each file found
for file in md_files:
    # read the contents of the file
    with open(file, 'r') as f:
        content = f.read()

    # parse the frontmatter using frontmatter library
    post = frontmatter.loads(content)

    # check if page field exists in the frontmatter
    if 'page' in post.keys():
        # rename page field to pageNum
        post['pageNum'] = post['page']
        del post['page']

        # construct new content with updated frontmatter and original markdown content
        new_contents = frontmatter.dumps(post) + post.content

        # write the updated contents back to the file
        with open(file, 'w') as f:
            f.write(new_contents)

        print(f"Updated {file}")
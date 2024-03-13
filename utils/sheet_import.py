import frontmatter
from frontmatter import Post
from pathlib import Path 
from csv import DictReader

umpire_path = Path('../umpire')
with open('/home/apjanco/Downloads/Index of articles printed at ESP - The Umpire.csv') as file:
    reader = DictReader(file)
    for row in reader:
        if row['id'] != '' and row['year']:
            post = Post(row['text'])
            post.metadata['id'] = row['id']
            post.metadata['title'] = row['title']
            post.metadata['author'] = row['author']
            post.metadata['newspaper'] = 'The Umpire'
            post.metadata['editor'] = row['editor']
            post.metadata['year'] = row['year']
            post.metadata['month'] = row['month']
            post.metadata['day'] = row['day']
            post.metadata['volume'] = row['volume']
            post.metadata['issue'] = row['issue']
            post.metadata['page'] = row['page']
            post.metadata['image'] = row['image']
            post.metadata['tags'] = row['tags'].split(';')
            post.metadata['layout'] = 'item'
            md = frontmatter.dumps(post)
            if not (umpire_path / row['year'] / 'items').exists():
                (umpire_path / row['year'] / 'items').mkdir(parents=True)
            (umpire_path / row['year'] / 'items' / f'{row["id"]}.md').write_text(md)

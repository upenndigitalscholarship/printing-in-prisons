import frontmatter
import pathlib

def no_layout():
    p = pathlib.Path('./umpire')
    for file_ in p.glob('**/*.md'):
        content = frontmatter.loads(file_.read_text())
        layout =  content.metadata.get('layout', None)
        if not layout:
            content.metadata['layout'] = 'item'
            file_.write_text(frontmatter.dumps(content))

def remove_duplicate_text():
    count = 0
    p = pathlib.Path('./umpire')
    for file_ in p.glob('**/*.md'):
        content = frontmatter.loads(file_.read_text())
        # find duplicate text
        text = content.content 
        start = text[:50]
        if text.find(start) !=  text.rfind(start):
            repeat = text.rfind(start)
            text = text[:repeat]
            content.content = text
            file_.write_text(frontmatter.dumps(content))
            count += 1
    print(count)
            

if __name__ == "__main__":
    #no_layout()
    remove_duplicate_text()
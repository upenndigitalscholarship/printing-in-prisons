import pathlib
p = pathlib.Path('./umpire-csv')
for file_ in p.glob('**/*.md'):
    txt = file_.read_text()
    output = """"""
    for row in txt.split('\n'):
        if 'title:' in row:
            if ":" in row[row.find('title:')+6:] and not '"' in row[row.find('title:')+6:]:
                title = row.find('title:')+6
                before = row[:title+1]
                after = row[title+1:]
                output += before + '"' + after + '"\n'
            else:    
                output += row +'\n'
        else:
            output += row +'\n'
    file_.write_text(output)
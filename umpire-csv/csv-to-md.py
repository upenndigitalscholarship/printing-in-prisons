import csv
from pathlib import Path 

def create_markdown_file(i, data_dict):
    # Create a new markdown file with the given file name
    year = [value for key, value in data_dict.items() if key == 'year'][0]
    year_folder = Path(f'./umpire/{year}')
    if not year_folder.exists(): 
        year_folder.mkdir(parents=True, exist_ok=True)
    file_name = f'./umpire/{year}/{i}'
    with open(file_name +  '.md', 'w') as f:
        # Write the frontmatter of the markdown file
        f.write('---\n')
        has_text = len([value for key, value in data_dict.items() if key == 'text'][0]) > 0
        
        for key, value in data_dict.items():
            
            if key and value:
                if key == 'text':
                    f.write('tags:\n')
                    f.write('layout: page.njk\n')
                    f.write('image:\n')
                    f.write('---\n')
                    f.write('{}\n'.format(value))
                else:
                    f.write('{}: {}\n'.format(key.lower(), value))
        if not has_text:
            f.write('tags:\n')
            f.write('layout: page.njk\n')
            f.write('image:\n')
            f.write('---\n')



if __name__ == '__main__':
    # Open and read the CSV file
    with open('umpire-full-text.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # Loop through each row of the CSV file
        for i, row in enumerate(reader):
            # Generate a file name based on the row number
            
            # Create a dictionary of data from the row
            data_dict = dict(row)
            # Create a markdown file with the data
            create_markdown_file(i, data_dict)

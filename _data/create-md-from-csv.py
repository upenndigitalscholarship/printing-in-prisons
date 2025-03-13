import csv
import os

def dict_to_yaml(data):
    """Convert dictionary to YAML frontmatter manually, adding single quotes around values."""
    yaml_str = '---\n'
    for key, value in data.items():
        yaml_str += f'{key}: "{value}"\n'  # Add quotes around the value
    yaml_str += '---\n'
    return yaml_str

def csv_to_markdown(csv_filename, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the CSV file and read it
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Loop through the rows in the CSV file
        for index, row in enumerate(reader):
            markdown_filename = os.path.join(output_folder, f'{index + 1}.md')
            
            # Create a dictionary for frontmatter (excluding 'text' column)
            frontmatter = {key: value for key, value in row.items() if key != 'text'}
            
            # Markdown file creation
            with open(markdown_filename, mode='w', encoding='utf-8') as markdown_file:
                # Write YAML frontmatter manually with single quotes around values
                markdown_file.write(dict_to_yaml(frontmatter))
                
                # Write 'text' content below frontmatter
                markdown_file.write(row.get('text', '') + '\n')
            
            print(f"Markdown file for row {index + 1} created: {markdown_filename}")

if __name__ == "__main__":
    csv_filename = 'easternecho.csv'  # Replace with your CSV file name
    output_folder = 'output_markdown'  # Folder to store the markdown files
    
    csv_to_markdown(csv_filename, output_folder)

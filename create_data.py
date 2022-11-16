#https://nanonets.com/blog/ocr-with-tesseract/
import cv2
import pytesseract
from pathlib import Path 
from tqdm import tqdm 
from rich import print 

image_path = Path('temp')
assets_path = Path('assets/img')

publication = 'echo'
year = '1966'
def main():
    for image in tqdm(image_path.iterdir(), total=212):
        img = cv2.imread(str(image))
        text = pytesseract.image_to_string(img)
        img_filename = f"{image.name}"
        frontmatter = """"""
        frontmatter += "---\n"
        frontmatter += f"title: {publication}\n"
        frontmatter += f"year: {year}\n"
        frontmatter += "tags:\n"
        frontmatter += f"layout: page.njk\n"
        frontmatter += f"image: {img_filename}\n"
        frontmatter += "---\n"

        filename = f"{image.stem}.md"
        text_path = Path(publication+'/'+year)
        if not text_path.exists():
            text_path.mkdir(parents=True, exist_ok=True)
        (text_path / filename).write_text(frontmatter + text)
        # Save image file to assets
        
        (assets_path / img_filename).write_bytes(image.read_bytes())
    print(f'[green bold] Completed [/green bold]')

if __name__ == "__main__":
    main()
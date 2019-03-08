import pytesseract
from PIL import Image
from PIL import ImageFilter


def extract_text_from_image(image_file_path):
    with open(image_file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.filter(ImageFilter.SHARPEN)
        text = pytesseract.image_to_string(image)
        return text
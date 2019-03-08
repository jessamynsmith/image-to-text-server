import pytesseract
from PIL import Image
from PIL import ImageFilter
import requests


def extract_text_from_image(image_file):
    image = Image.open(image_file)
    image.filter(ImageFilter.SHARPEN)
    text = pytesseract.image_to_string(image)
    return text


def extract_text_from_image_path(image_file_path):
    with open(image_file_path, 'rb') as image_file:
        return extract_text_from_image(image_file)


def extract_text_from_image_url(image_url):
    image_data = requests.get(image_url, stream=True).raw
    return extract_text_from_image(image_data)

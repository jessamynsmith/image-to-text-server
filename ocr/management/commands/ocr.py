from django.core.management.base import BaseCommand

from ocr.utils import extract_text_from_image


class Command(BaseCommand):
    help = 'Extract text from specified image'

    def add_arguments(self, parser):
        parser.add_argument(
            '--image-file',
            type=str,
            dest='image_file_path',
            required=True,
            help='Image from which to extract text'
        )

    def handle(self, *args, **options):
        image_file_path = options.get('image_file_path')
        text = extract_text_from_image(image_file_path)
        print(text)

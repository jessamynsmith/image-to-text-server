from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ocr.utils import extract_text_from_image, extract_text_from_image_url


class OcrDataView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'data' not in request.data:
            raise ParseError("Empty content")

        f = request.data['data']

        text = extract_text_from_image(f)
        print(text)
        return Response(text)


class OcrUrlView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        print(request.data)
        if 'data' not in request.data:
            raise ParseError("Empty content")

        url = request.data['data']

        text = extract_text_from_image_url(url)
        print(text)
        return Response(text)

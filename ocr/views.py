from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ocr.utils import extract_text_from_image


class OcrView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'data' not in request.data:
            raise ParseError("Empty content")

        f = request.data['data']

        text = extract_text_from_image(f)
        print(text)
        return Response(text)

from django.views.generic import FormView
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ocr import forms
from ocr.utils import extract_text_from_image, extract_text_from_image_url


class OcrDataApiView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'data' not in request.data:
            raise ParseError("Empty content")

        f = request.data['data']

        text = extract_text_from_image(f)
        return Response(text)


class OcrUrlApiView(APIView):

    def post(self, request, format=None):
        if 'url' not in request.data:
            raise ParseError("Empty content")

        url = request.data['url']

        text = extract_text_from_image_url(url)
        return Response(text)


class OcrUrlView(FormView):
    form_class = forms.UrlForm
    template_name = 'ocr/ocr_url_view.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.post(request, *args, **kwargs)

        return self.get(request, *args, **kwargs)

    def form_valid(self, form):
        self.image_url = form.cleaned_data.get('url')
        self.image_text = extract_text_from_image_url(self.image_url)
        self.ocr_attempted = True

    def form_invalid(self, form):
        print('Invalid form', form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['image_url'] = getattr(self, 'image_url', None)
        context_data['image_text'] = getattr(self, 'image_text', None)
        context_data['ocr_attempted'] = getattr(self, 'ocr_attempted', None)
        return context_data

from django.urls import path
from django.views.generic import RedirectView

from ocr import views


urlpatterns = [
    path('', RedirectView.as_view(url='/ocr/url/', permanent=False)),
    path('api/v1/ocr/data/', views.OcrDataApiView.as_view(), name='ocr_data'),
    path('api/v1/ocr/url/', views.OcrUrlApiView.as_view(), name='ocr_url'),
    path('ocr/url/', views.OcrUrlView.as_view(), name='ocr_url'),
]

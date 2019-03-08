from django.urls import path

from ocr import views


urlpatterns = [
    path('api/v1/ocr/data/', views.OcrDataView.as_view(), name='ocr_data'),
    path('api/v1/ocr/url/', views.OcrUrlView.as_view(), name='ocr_url'),
]

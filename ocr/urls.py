from django.urls import path

from ocr import views


urlpatterns = [
    path('api/v1/ocr/', views.OcrView.as_view(), name='ocr')
]

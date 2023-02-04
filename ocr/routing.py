from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/ocr/(?P<room_name>\w+)/$", consumers.OcrConsumer.as_asgi()),
]

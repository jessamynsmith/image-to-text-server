import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class OcrConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None

    def connect(self):
        # Partition data by user
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']

        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']

        # send generated data message event to the user's room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'ocr_message',
                'data': data,
            }
        )

    def ocr_message(self, event):
        self.send(text_data=json.dumps(event))

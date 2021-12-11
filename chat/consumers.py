import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # присоединяемся к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        print(f'SOCKET OPTIONS:\n\nROOM GROUP NAME: {self.room_group_name}\
            \n\nROOM NAME: {self.room_name}\
            \n\nROOM CHANNEL NAME: {self.channel_layer}')

        # принимаем подключение сокета
        await self.accept()

    async def disconnect(self, close_code):
        """ Отключаемся от комнаты группы """
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """ Получаем сообщение через вебсокет """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправляем СОБЫТИЕ/EVENT в группу
        # ключ type - имя метода, который вызывается, когда консумер получает событие
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )
    async def chat_message(self, event):
        """ Получаем сообщение от группы """
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
        }))
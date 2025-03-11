import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

logger = logging.getLogger(__name__)  # Логирование

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"  # Группа для комнаты

        logger.info(f"User {self.scope['user']} connected to room: {self.room_group_name}")  # Логирование

        # Добавляем пользователя в группу
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        logger.info(f"User {self.scope['user']} disconnected from room: {self.room_group_name}")  # Логирование

        # Удаляем пользователя из группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        logger.info(f"Received data: {text_data}")  # Логирование

        data = json.loads(text_data)
        sender_username = data['sender']
        message = data['message']

        # Сохраняем сообщение в базе данных
        sender = await self.get_user(sender_username)
        if sender:
            msg = await self.save_message(sender, message)

            # Отправляем сообщение в группу
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': msg.content,
                    'sender': sender.username
                }
            )

    async def chat_message(self, event):
        logger.info(f"Sending message to group: {self.room_group_name}")  # Логирование

        # Отправляем сообщение всем участникам группы
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))

    @sync_to_async
    def get_user(self, username):
        User = get_user_model()
        return User.objects.filter(username=username).first()

    @sync_to_async
    def save_message(self, sender, message):
        from .models import Message
        return Message.objects.create(sender=sender, room_name=self.room_name, content=message)
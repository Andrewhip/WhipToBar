import json
<<<<<<< HEAD
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
=======
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatMessage
from whiptobar.marketplace.models import Product
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if not self.scope["user"].is_authenticated:
            await self.close()  # Закрываем соединение, если пользователь не авторизован
            return

        self.product_id = self.scope['url_route']['kwargs']['product_id']
        try:
            self.product = await sync_to_async(Product.objects.get)(id=self.product_id)
        except Product.DoesNotExist:
            await self.close()  # Закрываем соединение, если товар не найден
            return

        self.room_group_name = f'chat_{self.product.id}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединяемся от комнаты
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
<<<<<<< HEAD
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
=======
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_username = self.scope['user'].username

        # Получаем товар и сохраняем сообщение асинхронно
        product = await sync_to_async(Product.objects.get)(id=self.product_id)
        chat_message = await sync_to_async(ChatMessage.objects.create)(
            sender=self.scope['user'],
            receiver=await sync_to_async(User.objects.get)(username="receiver_username"),
            product=product,
            message=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_username,
            }
        )

    async def chat_message(self, event):
        # Отправляем сообщение в WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

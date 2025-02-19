import json
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
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
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
<<<<<<< HEAD
from django.db import models
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Отправитель
    room_name = models.CharField(max_length=255)  # Название комнаты
    content = models.TextField()  # Текст сообщения
    timestamp = models.DateTimeField(auto_now_add=True)  # Время отправки

    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"


class ChatSession(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chat_sessions_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chat_sessions_as_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')  # Убедимся, что чат между двумя пользователями уникален

    def __str__(self):
        return f"Chat between {self.user1.username} and {self.user2.username}"

=======
# chat/models.py
from django.db import models
from django.contrib.auth.models import User
from marketplace.models import Product


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='messages')  # Привязка к товару
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}: {self.message}"
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832


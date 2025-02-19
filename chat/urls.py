from django.urls import path
from . import consumers

app_name = 'chat'  # Убедитесь, что указан правильный app_name

urlpatterns = [
    path('product_<int:product_id>/', consumers.ChatConsumer.as_asgi(), name='chat_product'),
]

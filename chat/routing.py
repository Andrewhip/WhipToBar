from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/product_<int:product_id>/', consumers.ChatConsumer.as_asgi()),
]


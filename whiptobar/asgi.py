"""
ASGI config for whiptobar project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

<<<<<<< HEAD
# asgi.py

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
<<<<<<< HEAD
from django.urls import path
from chat import routing
=======
import chat.routing
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whiptobar.settings')

application = ProtocolTypeRouter({
<<<<<<< HEAD
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
=======
    "http": get_asgi_application(),  # Обработка HTTP-запросов
    "websocket": AuthMiddlewareStack(  # Обработка WebSocket-запросов
        URLRouter(
            chat.routing.websocket_urlpatterns  # Маршруты WebSocket
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
        )
    ),
})

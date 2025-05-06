<<<<<<< HEAD
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
=======
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/product_<int:product_id>/', consumers.ChatConsumer.as_asgi()),
]

>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

from django.urls import path
<<<<<<< HEAD
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('user/<int:user_id>/', views.chat_room, name='chat_room'),
    path('load-messages/<str:room_name>/', views.load_messages, name='load_messages'),# Чат с конкретным пользователем
]
=======
from . import consumers

app_name = 'chat'  # Убедитесь, что указан правильный app_name

urlpatterns = [
    path('product_<int:product_id>/', consumers.ChatConsumer.as_asgi(), name='chat_product'),
]
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

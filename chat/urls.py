from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('user/<int:user_id>/', views.chat_room, name='chat_room'),
    path('load-messages/<str:room_name>/', views.load_messages, name='load_messages'),# Чат с конкретным пользователем
]
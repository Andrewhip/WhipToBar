<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import Message, ChatSession
import logging
from django.http import JsonResponse
from django.core.serializers import serialize

logger = logging.getLogger(__name__)  # Логирование

User = get_user_model()

@login_required
def chat_room(request, user_id):
    other_user = get_object_or_404(User, id=user_id)

    # Запрещаем пользователю заходить в чат с самим собой
    if request.user.id == other_user.id:
        return redirect('chat:chat_list')

    # Проверяем, существует ли уже чат между пользователями
    chat = ChatSession.objects.filter(
        Q(user1=request.user, user2=other_user) | Q(user1=other_user, user2=request.user)
    ).first()

    # Если чата нет, создаем его
    if not chat:
        chat = ChatSession.objects.create(
            user1=request.user,
            user2=other_user
        )
        logger.info(f"Created new chat between {request.user.username} and {other_user.username}")

    # Генерируем уникальное имя комнаты для двоих пользователей
    user_ids = sorted([request.user.id, other_user.id])
    room_name = f"chat_{user_ids[0]}_{user_ids[1]}"
    logger.info(f"Room name: {room_name}")  # Логирование

    # Загружаем последние 10 сообщений между пользователями
    messages = Message.objects.filter(
        room_name=room_name
    ).order_by('-timestamp')[:10]  # Последние 10 сообщений
    messages = reversed(messages)  # Обратный порядок для корректного отображения

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'current_user': request.user,
        'other_user': other_user,
        'messages': messages,
        'offset': 10,  # Начальный offset для следующей загрузки
    })

@login_required
def chat_list(request):
    # Получаем все чаты, где текущий пользователь является user1 или user2
    chats = ChatSession.objects.filter(Q(user1=request.user) | Q(user2=request.user))

    # Для каждого чата определяем, кто второй участник
    chat_partners = []
    for chat in chats:
        if chat.user1 == request.user:
            partner = chat.user2
        else:
            partner = chat.user1
        chat_partners.append({
            'partner': partner,
            'chat_id': chat.id,
        })

    return render(request, 'chat/chat_list.html', {
        'chat_partners': chat_partners,
    })


from django.http import JsonResponse
from django.core.serializers import serialize

@login_required
def load_messages(request, room_name):
    offset = int(request.GET.get('offset', 0))

    # Загружаем старые сообщения
    messages = Message.objects.filter(
        room_name=room_name
    ).order_by('-timestamp')[offset:offset + 10]  # Загружаем по 10 сообщений
    messages = reversed(messages)

    # Преобразуем сообщения в JSON
    serialized_messages = []
    for message in messages:
        serialized_messages.append({
            'content': message.content,
            'sender': message.sender.username,
            'timestamp': message.timestamp.strftime('%H:%M'),
            'avatar_url': message.sender.photo.url if message.sender.photo else "/media/users/default.jpg",
        })

    return JsonResponse({'messages': serialized_messages})
=======
from django.shortcuts import render

def chat_view(request):
    return render(request, 'chat/chat_room.html')
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

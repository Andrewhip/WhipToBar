import requests
from django.core.files.base import ContentFile
from ..models import Post
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

def take_50_posts():
    TOKEN = os.getenv("VK_API_TOKEN")  # Теперь токен не в коде
    version = 5.199
    domain = 'insidebmxru'  # Ваше сообщество
    count = 50

    response = requests.get(
        'https://api.vk.com/method/wall.get',
        params={
            'access_token': TOKEN,
            'v': version,
            'domain': domain,
            'count': count,
            'extended': 1,  # Для получения вложений
        }
    )

    try:
        data = response.json()['response']['items']
    except KeyError:
        print("Ошибка: ответ API не содержит ожидаемого ключа 'response'. Ответ:")
        print(response.json())
        return []

    print(f"Получено постов: {len(data)}")  # Печатаем количество полученных постов

    created_count = 0  # Счётчик созданных постов
    for post in data:
        text = post.get('text', '')
        video_iframe = None
        image_file = None

        attachments = post.get('attachments', [])
        for attachment in attachments:
            if attachment.get('type') == 'video':
                video_data = attachment['video']
                owner_id = video_data['owner_id']
                video_id = video_data['id']
                access_key = video_data.get('access_key', '')

                video_iframe = (
                    f'<iframe src="https://vk.com/video_ext.php?oid={owner_id}&id={video_id}&hash={access_key}&hd=2" '
                    f'width="853" height="480" allow="autoplay; encrypted-media; fullscreen; picture-in-picture;" '
                    f'frameborder="0" allowfullscreen></iframe>'
                )
                print(f"Video URL: https://vk.com/video_ext.php?oid={owner_id}&id={video_id}&hash={access_key}&hd=2")  # Печать ссылки
            elif attachment.get('type') == 'photo':
                # Извлекаем URL на самое большое фото
                sizes = attachment['photo']['sizes']
                image_url = max(sizes, key=lambda size: size['width'])['url']

                # Загружаем изображение
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_name = os.path.basename(urlparse(image_url).path)
                    image_file = ContentFile(response.content, name=image_name)

        # Создаем или обновляем запись в базе данных
        post, created = Post.objects.get_or_create(
            text=text,
            video_url=video_iframe,  # Сохраняем iframe в поле video_url
        )

        # Если был добавлен файл изображения, обновляем поле image
        if created and image_file:
            post.image.save(image_file.name, image_file, save=True)
            created_count += 1

    print(f"Создано новых постов: {created_count}")
    return data


# Вызов функции для добавления постов
posts = take_50_posts()

# Печать количества добавленных постов
print(f"Всего обработано постов: {len(posts)}")

# Печать всех постов (если необходимо для отладки)
for post in posts:
    print(post)


from django.db import models
<<<<<<< HEAD
from django.conf import settings
from django.utils import timezone
from rest_framework.reverse import reverse

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

class Post(models.Model):
    SOURCE_CHOICES = [
        ('parser', 'Парсер'),
        ('manual', 'Вручную'),
    ]

    text = models.TextField()  # Основное содержимое поста
<<<<<<< HEAD
    published_at = models.DateTimeField(auto_now_add=True,)  # Дата публикации
=======
    published_at = models.DateTimeField(auto_now_add=True)  # Дата публикации
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
    video_url = models.TextField(null=True, blank=True)  # Ссылка на видео
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)  # Загруженное видео
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)  # Изображение
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default='manual')  # Источник

    def __str__(self):
<<<<<<< HEAD
        return self.text[:50]  # Для отображения в админке используем первые 50 символов текста

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Связь с User
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

    def user_photo(self):
        """Метод для получения фото пользователя или дефолтного фото"""
        return self.user.photo.url if self.user.photo else '/media/users/default.jpg'
=======
        return self.text[:50]  # Для отображения в админке используем первые 50 символов текста
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

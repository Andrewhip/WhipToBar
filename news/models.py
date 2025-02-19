from django.db import models

class Post(models.Model):
    SOURCE_CHOICES = [
        ('parser', 'Парсер'),
        ('manual', 'Вручную'),
    ]

    text = models.TextField()  # Основное содержимое поста
    published_at = models.DateTimeField(auto_now_add=True)  # Дата публикации
    video_url = models.TextField(null=True, blank=True)  # Ссылка на видео
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)  # Загруженное видео
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)  # Изображение
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default='manual')  # Источник

    def __str__(self):
        return self.text[:50]  # Для отображения в админке используем первые 50 символов текста
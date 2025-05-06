from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .utils import send_telegram_message  # Импортируем асинхронную функцию
import asyncio

@receiver(post_save, sender=Product)
def notify_about_new_product(sender, instance, created, **kwargs):
    if created:
        message = (
            "Новый товар добавлен!\n\n"
            f"Название: {instance.name}\n"
            f"Ссылка: http://whiptobar.ru{instance.get_absolute_url()}"
        )
        asyncio.run(send_telegram_message(message))  # Используем asyncio.run
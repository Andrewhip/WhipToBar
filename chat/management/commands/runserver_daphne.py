from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Запускает сервер daphne'

    def handle(self, *args, **kwargs):
        os.system('daphne -b 0.0.0.0 -p 8000 whiptobar.asgi:application')
import aiohttp
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Токен бота и Chat ID
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Асинхронная функция для отправки сообщений
async def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            return await response.json()
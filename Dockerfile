# Базовый образ Python
FROM python:3.12-slim

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Установите переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Установите зависимости системы (если нужны)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Скопируйте requirements.txt в контейнер
COPY requirements.txt .

# Установите Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы проекта
COPY . .

# Команда для запуска приложения через Daphne
CMD ["daphne", "whiptobar.asgi:application", "-b", "0.0.0.0", "-p", "8000"]
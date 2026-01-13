# Базовый образ Python
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY ./src ./src

# Экспонируем порт для FastAPI
EXPOSE 8000

# Команда запуска приложения
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]


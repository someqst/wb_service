FROM python:3.12-slim

# Установим системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /wb_service

# Копируем только файлы зависимостей
COPY pyproject.toml /wb_service/

# Устанавливаем uv
RUN pip install uv

# Устанавливаем зависимости
RUN uv pip install -r pyproject.toml

# Копируем остальные файлы проекта
COPY . /wb_service
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

class Config:
    # Параметры базы данных
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///financial_operations.db")
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Прочие настройки
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

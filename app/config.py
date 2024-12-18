import os
import logging
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Настройка логгера
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Config:
    # Параметры базы данных
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///financial_operations.db")
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Прочие настройки
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    @staticmethod
    def init_app(app):
        """
        Инициализация приложения с текущими настройками конфигурации.
        """
        if Config.DEBUG:
            logger.warning("Приложение работает в режиме отладки. Убедитесь, что это не используется в продакшене.")
        
        if Config.SECRET_KEY == "default-secret-key":
            logger.warning("Используется ключ по умолчанию. Это небезопасно для продакшена.")

# Функция для загрузки конфигурации на основе имени окружения
def load_config(env_name):
    config_classes = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }
    return config_classes.get(env_name, Config)

# Конфигурация для разработки
class DevelopmentConfig(Config):
    DEBUG = True

# Конфигурация для тестирования
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Использование базы данных в памяти

# Конфигурация для продакшена
class ProductionConfig(Config):
    DEBUG = False
    # Проверка на обязательные переменные окружения для продакшена
    required_env_vars = ["DATABASE_URL", "SECRET_KEY"]

    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"Отсутствуют обязательные переменные окружения: {', '.join(missing_vars)}")

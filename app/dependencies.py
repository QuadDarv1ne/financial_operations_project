# *******************************************************
# app/dependencies.py                                   #
# *******************************************************
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.config import Config  # Импортируем конфиг, чтобы получить доступ к переменным

# Настройка логгера
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Настройка SQLAlchemy с использованием правильной переменной
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Логируем создание и закрытие сессий
logger.info(f"Создано подключение к базе данных: {Config.SQLALCHEMY_DATABASE_URL}")

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        logger.info("Создана новая сессия базы данных")
        yield db
    finally:
        db.close()
        logger.info("Сессия базы данных закрыта")

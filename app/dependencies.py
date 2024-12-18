# *******************************************************
# app/dependencies.py                                   #
# *******************************************************
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.config import Config  # Импортируем конфиг, чтобы получить доступ к переменным

# Настройка SQLAlchemy с использованием правильной переменной
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)  # Используем Config.SQLALCHEMY_DATABASE_URL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# *******************************************************
# app/models.py                                         #
# *******************************************************
from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from enum import Enum as PyEnum
import bcrypt  # Для хеширования паролей

from app.config import Config  # Импортируем Config класс

# Настройка базы данных с использованием конфигурации из config.py
Base = declarative_base()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Модели базы данных

class TransactionType(PyEnum):
    """
    Тип транзакции (доход/расход).
    Используется для определения типа транзакции в модели Transaction.
    """
    INCOME = "доход"
    EXPENSE = "расход"

class User(Base):
    """
    Модель пользователя.
    Хранит данные пользователя, такие как имя пользователя, email, хеш пароля.
    Также включает связи с аккаунтами, категориями и транзакциями пользователя.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)  # Уникальное имя пользователя
    email = Column(String, unique=True, index=True, nullable=False)      # Уникальный email пользователя
    password_hash = Column(String, nullable=False)  # Хеш пароля
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата создания пользователя

    # Связи с другими таблицами
    accounts = relationship("Account", back_populates="user")  # Аккаунты пользователя
    categories = relationship("Category", back_populates="user")  # Категории пользователя
    transactions = relationship("Transaction", back_populates="user")  # Транзакции пользователя

    def check_password(self, password: str) -> bool:
        """
        Проверка пароля пользователя.
        Сравнивает введенный пароль с сохраненным хешем пароля.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def set_password(self, password: str) -> None:
        """
        Установка хеша пароля.
        """
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

class Account(Base):
    """
    Модель аккаунта.
    Хранит данные об аккаунте пользователя, включая баланс и дату создания.
    """
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Ссылка на пользователя
    name = Column(String, nullable=False)  # Название аккаунта
    balance = Column(Float, default=0)  # Баланс на аккаунте, по умолчанию 0
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата создания аккаунта

    # Связи с другими таблицами
    user = relationship("User", back_populates="accounts")  # Связь с пользователем
    transactions = relationship("Transaction", back_populates="account")  # Связь с транзакциями

class Category(Base):
    """
    Модель категории.
    Хранит категории, используемые для классификации транзакций.
    """
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Ссылка на пользователя
    name = Column(String, nullable=False)  # Название категории
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата создания категории

    # Связи с другими таблицами
    user = relationship("User", back_populates="categories")  # Связь с пользователем
    transactions = relationship("Transaction", back_populates="category")  # Связь с транзакциями

class Transaction(Base):
    """
    Модель транзакции.
    Хранит данные о транзакции: тип, сумма, дата и описание.
    """
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Ссылка на пользователя
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)  # Ссылка на аккаунт
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)  # Ссылка на категорию
    type = Column(Enum(TransactionType), nullable=False)  # Тип транзакции (доход/расход)
    amount = Column(Float, nullable=False)  # Сумма транзакции
    description = Column(String)  # Описание транзакции
    transaction_date = Column(DateTime, default=datetime.utcnow)  # Дата транзакции

    # Связи с другими таблицами
    user = relationship("User", back_populates="transactions")  # Связь с пользователем
    account = relationship("Account", back_populates="transactions")  # Связь с аккаунтом
    category = relationship("Category", back_populates="transactions")  # Связь с категорией

# Функция для создания таблиц
def create_tables():
    """
    Создание всех таблиц в базе данных.
    Если таблицы уже существуют, они не будут созданы заново.
    """
    Base.metadata.create_all(bind=engine)

# Вызов функции для создания таблиц при старте приложения
create_tables()

# *******************************************************
# app/schemas.py                                        #
# *******************************************************
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Описание схем для создания и получения данных

class CategoryCreate(BaseModel):
    """
    Схема для создания новой категории.
    Используется для валидации данных при создании категории.
    """
    name: str  # Название категории

    class Config:
        from_attributes = True


class CategoryOut(BaseModel):
    """
    Схема для отображения данных о категории.
    Используется для получения данных о категории.
    """
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class AccountCreate(BaseModel):
    """
    Схема для создания нового аккаунта.
    """
    name: str  # Название аккаунта

    class Config:
        from_attributes = True


class AccountOut(BaseModel):
    """
    Схема для отображения данных об аккаунте.
    """
    id: int
    name: str
    balance: float
    created_at: datetime

    class Config:
        from_attributes = True


class TransactionCreate(BaseModel):
    """
    Схема для создания новой транзакции.
    """
    account_id: int
    category_id: int
    type: str  # Тип транзакции (доход или расход)
    amount: float  # Сумма транзакции
    description: Optional[str] = None  # Описание транзакции

    class Config:
        from_attributes = True


class TransactionOut(BaseModel):
    """
    Схема для отображения данных о транзакции.
    """
    id: int
    account_id: int
    category_id: int
    type: str  # Тип транзакции (доход или расход)
    amount: float
    description: Optional[str] = None
    transaction_date: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    """
    Схема для создания нового пользователя.
    """
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    """
    Схема для отображения данных о пользователе.
    """
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

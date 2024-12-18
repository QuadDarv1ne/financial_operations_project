# ***********************************************************
# app/routes/__init__.py                                    #
# ***********************************************************
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models import User, Account, Category, Transaction, engine, SessionLocal
from app.schemas import UserCreate, UserOut, AccountCreate, AccountOut, CategoryCreate, CategoryOut, TransactionCreate, TransactionOut
from app import crud  # Допустим, у вас есть отдельный файл для CRUD-операций

# Создаем маршруты для работы с пользователями, аккаунтами, категориями и транзакциями
router = APIRouter()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания нового пользователя
@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# Маршрут для получения списка всех пользователей
@router.get("/users/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Маршрут для получения пользователя по ID
@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Маршрут для создания нового аккаунта
@router.post("/accounts/", response_model=AccountOut, status_code=status.HTTP_201_CREATED)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db=db, account=account)

# Маршрут для получения всех аккаунтов пользователя
@router.get("/accounts/{user_id}", response_model=List[AccountOut])
def get_accounts(user_id: int, db: Session = Depends(get_db)):
    return crud.get_accounts_by_user(db, user_id=user_id)

# Маршрут для создания новой категории
@router.post("/categories/", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

# Маршрут для получения всех категорий пользователя
@router.get("/categories/{user_id}", response_model=List[CategoryOut])
def get_categories(user_id: int, db: Session = Depends(get_db)):
    return crud.get_categories_by_user(db, user_id=user_id)

# Маршрут для создания новой транзакции
@router.post("/transactions/", response_model=TransactionOut, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

# Маршрут для получения всех транзакций пользователя
@router.get("/transactions/{user_id}", response_model=List[TransactionOut])
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions_by_user(db, user_id=user_id)

# Маршрут для получения всех транзакций по аккаунту
@router.get("/transactions/account/{account_id}", response_model=List[TransactionOut])
def get_transactions_by_account(account_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions_by_account(db, account_id=account_id)

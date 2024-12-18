from sqlalchemy.orm import Session
from app.models import User, Account, Category, Transaction
from app.schemas import UserCreate, AccountCreate, CategoryCreate, TransactionCreate
from typing import List, Optional

# Функции для работы с пользователями

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    Получить пользователя по email.
    """
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """
    Получить пользователя по ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session) -> List[User]:
    """
    Получить всех пользователей.
    """
    return db.query(User).all()

def create_user(db: Session, user: UserCreate) -> User:
    """
    Создать нового пользователя.
    """
    db_user = User(username=user.username, email=user.email)
    db_user.set_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Функции для работы с аккаунтами

def get_accounts_by_user(db: Session, user_id: int) -> List[Account]:
    """
    Получить все аккаунты пользователя.
    """
    return db.query(Account).filter(Account.user_id == user_id).all()

def create_account(db: Session, account: AccountCreate) -> Account:
    """
    Создать новый аккаунт.
    """
    db_account = Account(user_id=account.user_id, name=account.name, balance=account.balance)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

# Функции для работы с категориями

def get_categories_by_user(db: Session, user_id: int) -> List[Category]:
    """
    Получить все категории пользователя.
    """
    return db.query(Category).filter(Category.user_id == user_id).all()

def create_category(db: Session, category: CategoryCreate) -> Category:
    """
    Создать новую категорию.
    """
    db_category = Category(user_id=category.user_id, name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Функции для работы с транзакциями

def get_transactions_by_user(db: Session, user_id: int) -> List[Transaction]:
    """
    Получить все транзакции пользователя.
    """
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()

def get_transactions_by_account(db: Session, account_id: int) -> List[Transaction]:
    """
    Получить все транзакции по аккаунту.
    """
    return db.query(Transaction).filter(Transaction.account_id == account_id).all()

def create_transaction(db: Session, transaction: TransactionCreate) -> Transaction:
    """
    Создать новую транзакцию.
    """
    db_transaction = Transaction(
        user_id=transaction.user_id,
        account_id=transaction.account_id,
        category_id=transaction.category_id,
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

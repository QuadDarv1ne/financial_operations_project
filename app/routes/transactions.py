from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Transaction
from app.schemas import TransactionCreate
from app.dependencies import get_db

router = APIRouter()

@router.post("/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    new_transaction = Transaction(
        user_id=transaction.user_id,
        account_id=transaction.account_id,
        category_id=transaction.category_id,
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return {"message": "Транзакция добавлена", "id": new_transaction.id}

@router.get("/")
def list_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

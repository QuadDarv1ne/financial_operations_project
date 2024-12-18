from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Transaction
from app.schemas import TransactionCreate, TransactionResponse
from app.dependencies import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=TransactionResponse)
async def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
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
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[TransactionResponse])
async def list_transactions(db: Session = Depends(get_db)):
    try:
        transactions = db.query(Transaction).all()
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

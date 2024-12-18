from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Account
from app.schemas import AccountCreate
from app.dependencies import get_db

router = APIRouter()

@router.post("/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    new_account = Account(user_id=account.user_id, name=account.name, balance=account.balance)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return {"message": "Счет создан", "id": new_account.id, "balance": new_account.balance}

@router.get("/{account_id}")
def get_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Счет не найден.")
    return account

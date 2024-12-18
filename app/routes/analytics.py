from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Transaction
from app.dependencies import get_db

router = APIRouter()

@router.get("/summary")
def get_summary(user_id: int, db: Session = Depends(get_db)):
    income = db.query(Transaction).filter(Transaction.user_id == user_id, Transaction.type == "доход").all()
    expense = db.query(Transaction).filter(Transaction.user_id == user_id, Transaction.type == "расход").all()
    total_income = sum(t.amount for t in income)
    total_expense = sum(t.amount for t in expense)
    return {"total_income": total_income, "total_expense": total_expense, "balance": total_income - total_expense}

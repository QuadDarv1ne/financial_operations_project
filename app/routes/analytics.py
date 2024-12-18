from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Transaction
from app.dependencies import get_db

router = APIRouter()

@router.get("/summary")
def get_summary(user_id: int, db: Session = Depends(get_db)):
    try:
        # Получение общего дохода и расхода напрямую из базы данных
        total_income = db.query(func.sum(Transaction.amount)).filter(Transaction.user_id == user_id, Transaction.type == "доход").scalar() or 0
        total_expense = db.query(func.sum(Transaction.amount)).filter(Transaction.user_id == user_id, Transaction.type == "расход").scalar() or 0

        # Вычисление баланса
        balance = total_income - total_expense

        return {"total_income": total_income, "total_expense": total_expense, "balance": balance}
    except Exception as e:
        # Обработка исключений и возврат соответствующего сообщения об ошибке
        raise HTTPException(status_code=500, detail=str(e))

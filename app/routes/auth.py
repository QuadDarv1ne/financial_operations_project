# ***************************************************
# app/routes/auth.py                                #
# ***************************************************
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.dependencies import get_db
from app.utils import hash_password

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован.")
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Регистрация успешна", "id": new_user.id}

@router.post("/login")
def login_user():
    # Реализация логики входа
    return {"message": "Логин успешен"}

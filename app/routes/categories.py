from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate
from app.dependencies import get_db

router = APIRouter()

@router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(user_id=category.user_id, name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"message": "Категория создана", "id": new_category.id}

@router.get("/")
def list_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories

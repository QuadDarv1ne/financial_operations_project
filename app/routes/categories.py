from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate, CategoryResponse
from app.dependencies import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        new_category = Category(user_id=category.user_id, name=category.name)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return {"message": "Категория создана", "id": new_category.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[CategoryResponse])
async def list_categories(db: Session = Depends(get_db)):
    try:
        categories = db.query(Category).all()
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

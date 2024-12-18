# *******************************************************
# app/__init__.py                                       #
# *******************************************************
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import Config

Base: DeclarativeMeta = declarative_base()

# Создаём движок базы данных
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL, echo=Config.SQLALCHEMY_ECHO)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

templates = Jinja2Templates(directory="app/templates")

def create_app() -> FastAPI:
    app = FastAPI(debug=Config.DEBUG)
    
    # Подключение маршрутов
    from app.routes import auth, accounts, categories, transactions, analytics
    app.include_router(auth.router)
    app.include_router(accounts.router)
    app.include_router(categories.router)
    app.include_router(transactions.router)
    app.include_router(analytics.router)
    
    # Подключение статических файлов
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    
    return app

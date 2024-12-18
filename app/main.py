from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Настройка пути к директории с шаблонами
templates = Jinja2Templates(directory="app/templates")

# Настройка статических файлов (если есть)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard")
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/login")
async def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
async def read_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/account_details")
async def read_account_details(request: Request):
    return templates.TemplateResponse("account_details.html", {"request": request})

@app.get("/analytics")
async def read_analytics(request: Request):
    return templates.TemplateResponse("analytics.html", {"request": request})

@app.get("/transaction_list")
async def read_transaction_list(request: Request):
    return templates.TemplateResponse("transaction_list.html", {"request": request})

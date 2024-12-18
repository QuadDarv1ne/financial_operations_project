from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard")
async def read_dashboard(request: Request):
    user = {"username": "QuadDarv1ne"}
    accounts = [
        {"id": 1, "name": "Основной счет", "balance": 1000.0},
        {"id": 2, "name": "Сберегательный счет", "balance": 5000.0}
    ]
    transactions = [
        {"date": "2024-12-17", "amount": 100.0, "type": "income"},
        {"date": "2024-12-16", "amount": 50.0, "type": "expense"}
    ]
    return templates.TemplateResponse("dashboard.html", {
        "request": request, 
        "user": user, 
        "accounts": accounts, 
        "transactions": transactions
    })

@app.get("/auth/login")
async def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/auth/login")
async def process_login(email: str, password: str):
    return {"message": "Login successful", "email": email}

@app.get("/auth/register")
async def read_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/auth/register")
async def process_register(username: str, email: str, password: str):
    return {"message": "Registration successful", "username": username}

@app.get("/accounts/{account_id}")
async def read_account_details(request: Request, account_id: int):
    account = {"name": "Основной счет", "balance": 1000.0}
    transactions = [
        {"date": "2024-12-17", "amount": 100.0, "type": "income"},
        {"date": "2024-12-16", "amount": 50.0, "type": "expense"}
    ]
    return templates.TemplateResponse("account_details.html", {
        "request": request,
        "account": account,
        "transactions": transactions
    })

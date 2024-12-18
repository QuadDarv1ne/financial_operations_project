from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>Главная страница</title>
        </head>
        <body>
            <h1>Добро пожаловать на главную страницу!</h1>
            <p>Это главная страница вашего сайта.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

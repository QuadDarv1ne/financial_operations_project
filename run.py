# ***********************************************
# run.py                                        #
# ***********************************************
import uvicorn
import logging
import os
from app import create_app

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получение параметров конфигурации из переменных окружения
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
RELOAD = os.getenv("RELOAD", "False").lower() == "true"

app = create_app()

if __name__ == "__main__":
    logger.info(f"Запуск сервера на {HOST}:{PORT}, Reload: {RELOAD}")
    uvicorn.run(app, host=HOST, port=PORT, reload=RELOAD)

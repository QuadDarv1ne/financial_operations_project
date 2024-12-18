# ***********************************************
# app/utils.py                                  #
# ***********************************************
import bcrypt
from typing import Optional

def hash_password(password: str) -> str:
    """
    Хэширует пароль с использованием bcrypt.
    
    :param password: Пароль в виде строки
    :return: Хэшированный пароль в виде строки
    """
    # Генерация соли для хэширования
    salt = bcrypt.gensalt()
    # Хэширование пароля с использованием соли
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Возвращение хэшированного пароля в виде строки
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Проверяет пароль с использованием таймингово-защищенного сравнения.
    
    :param password: Пароль в виде строки
    :param hashed_password: Хэшированный пароль в виде строки
    :return: True, если пароли совпадают, иначе False
    """
    # Сравнение пароля с хэшированным паролем
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_salt(rounds: Optional[int] = 12) -> str:
    """
    Генерирует соль для хэширования пароля.
    
    :param rounds: Количество раундов для генерации соли (по умолчанию 12)
    :return: Соль в виде строки
    """
    # Генерация соли с указанным количеством раундов
    return bcrypt.gensalt(rounds).decode('utf-8')

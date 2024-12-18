# ***********************************************
# app/utils.py                                  #
# ***********************************************
import bcrypt

def hash_password(password: str) -> str:
    """Хэширует пароль с использованием bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

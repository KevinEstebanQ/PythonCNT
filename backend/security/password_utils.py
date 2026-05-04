from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from db.users.users import User


password_hash = PasswordHash.recommended()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(plain_password: str)->str:
    return password_hash.hash(plain_password)



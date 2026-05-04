from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from pydanticModels.UserModels import * 
from db.users.users import User
from fastapi import HTTPException
from security.password_utils import get_password_hash
from security.password_utils import verify_password

def create_user(body: UserIn, db: Session)-> UserOut:
    if not body.username or not body.password or not body.email:
        raise HTTPException(status_code=400, detail="Not Enough Information")

    stmt = select(User).where(User.username == body.username)
    result = db.scalar(stmt)
    if result:
        raise HTTPException(status_code=409, detail="resource already exists")
    stmt = select(User).where(User.email == body.email)
    result = db.scalar(stmt)
    if result:
        raise HTTPException(status_code=409, detail="resource already exists")
    newUser = User(username=body.username, password=get_password_hash(body.password), email=body.email)

    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return UserOut(username=body.username, email=body.email)

def get_user_db(email:str,  db: Session)->User:
    stmt = select(User).where(User.email == email)
    result = db.scalar(stmt)
    return result

def authenticate_user(db: Session, email: str, password: str)-> User | None:
    user = get_user_db(email=email, db=db)
    if not user:
        return None
    if verify_password(password, user.password):
        return user
    return None
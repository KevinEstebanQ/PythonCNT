from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.init_db import init_db
from crud.user_crud import get_user_db
from fastapi import Depends
from configs.load_configs import load_configs
import jwt
import os
from db.users.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
load_configs()
config = os.environ

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(init_db))->User:
    credentials_exc = HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, config["SECRET_KEY"], algorithms=[config["ALGORITHM"]])
    except jwt.exceptions.InvalidTokenError:
        raise credentials_exc
    email = payload.get("sub")
    if not email:
        raise credentials_exc
    user = get_user_db(email=email, db=db)
    if not user:
        raise credentials_exc
    return user
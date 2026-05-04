import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
import os
from fastapi import HTTPException
from pydanticModels.tokenModels import TokenData



def create_access_token(data: dict, delta: timedelta | None = None):
    data = data.copy()
    if delta:
        expire = datetime.now(timezone.utc) + delta
    else: 
        minutes = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
        expire = datetime.now(timezone.utc) + timedelta(minutes=minutes)

    algorithm = os.environ.get("ALGORITHM", "HS256")
    secret_key = os.environ.get("SECRET_KEY", None)
    if not secret_key:
        raise ValueError
    data.update({"exp": expire})
    jwt_encoded = jwt.encode(payload=data, key= secret_key ,algorithm=algorithm)
    return jwt_encoded

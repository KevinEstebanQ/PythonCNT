from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserIn(UserBase):
    password: str
    email: str
    username: str

class UserOut(UserBase):
    date: datetime = datetime.now()
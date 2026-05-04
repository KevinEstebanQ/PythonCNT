from db.base import BaseClass
from typing import List
from sqlalchemy import String, Text, DateTime, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class User(BaseClass):
    """ users table in database """
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    notes: Mapped[List["Note"]] = relationship(back_populates="user", cascade="all, delete-orphan", passive_deletes=True)

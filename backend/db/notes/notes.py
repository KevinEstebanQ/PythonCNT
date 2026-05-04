from db.base import BaseClass
from typing import List
from sqlalchemy import ForeignKey, String, DateTime, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Note(BaseClass):
    """ Notes table in database """
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(String(255))
    date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates="notes")
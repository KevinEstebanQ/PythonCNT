from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import BaseClass
from .notes.notes import Note
from .users.users import User
from pathlib import Path

db_path = Path(__file__).resolve().parent.parent.parent / "db" / "mydb.db"
engine = create_engine(f"sqlite:///{db_path}")
BaseClass.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
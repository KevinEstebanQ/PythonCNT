from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select, update, join, insert, delete
from db.init_db import init_db
from db.notes.notes import Note
from db.users.users import User
from pydanticModels.notesModels import NewNote, NewNoteIn, NoteOut, UpdateNote, NoteOutSingle
from deps.fast_api_deps import get_current_user
from datetime import datetime

def create_new_note(content:str, user: User, db: Session) -> NewNote:
    
    date = datetime.now()
    newNote = Note(data = content, date = date, user_id=user.id)
    db.add(newNote)
    db.commit()
    db.refresh(newNote)
    return NewNote(data=content, date_created=date, user_id=user.id)

def _get_user_notes(db: Session, user: User)->NoteOut:
    stmt = select(Note).where(Note.user_id == user.id)
    result = db.scalars(stmt).all()
    output = [NoteOutSingle(id=note.id, data=note.data, date_created=note.date, user_id=note.user_id) for note in result]
    return NoteOut(notes=output)

def edit_note(db: Session, id: int, data: str) -> UpdateNote:
    stmt = update(Note).where(Note.id == id).values(data=data, date=datetime.now())
    db.execute(stmt)
    db.commit()
    stmt = select(Note).where(Note.id == id)
    result = db.scalar(stmt)
    return UpdateNote(data=result.data, date_modified=result.date)

def delete_note(db: Session, id: int):
    stmt = delete(Note).where(Note.id == id).returning(Note.id)
    result = db.scalars(stmt).first()
    db.commit()
    return result


    
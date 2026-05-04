from typing import List

from pydantic import BaseModel
from datetime import datetime

class NewNote(BaseModel):
    data: str
    date_created: datetime
    user_id: int

class NewNoteIn(BaseModel):
    data: str

class NoteOutSingle(NewNote):
    id: int

class NoteOut(BaseModel):
    notes: List[NoteOutSingle]

class UpdateNote(BaseModel):
    data:str
    date_modified: datetime
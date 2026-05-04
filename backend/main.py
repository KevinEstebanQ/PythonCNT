from datetime import timedelta

from fastapi import FastAPI,HTTPException 
from fastapi import Depends
from typing import Annotated
from configs.load_configs import load_configs
from db.init_db import init_db
from db.users.users import User
from crud.user_crud import authenticate_user, create_user, get_user_db
from crud.notes_crud import create_new_note, _get_user_notes, edit_note, delete_note
from pydanticModels.notesModels import NewNote, NewNoteIn, NoteOut
from sqlalchemy.orm import Session
from pydanticModels.UserModels import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from security.token import create_access_token
from pydanticModels.tokenModels import Token, TokenData
from pydanticModels.notesModels import NewNote, NewNoteIn, UpdateNote
from deps.fast_api_deps import get_current_user, oauth2_scheme
import jwt
import os
from configs.load_configs import load_configs

load_configs()
config = os.environ


app = FastAPI()



@app.get("/health")
def get_health():
    return {"message": "ok"}, 200

@app.post("/user", response_model=UserOut)
def post_user(body: UserIn, db: Session = Depends(init_db)):
    return create_user(body, db)

@app.post("/login")
def login(body: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(init_db)):
    # authenticate and get user via credentials
    user = authenticate_user(db=db, email=body.username, password=body.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    # create new short lived access token for user vian env vars
    access_token_expires = timedelta(minutes=int(config["ACCESS_TOKEN_EXPIRE_MINUTES"]))

    # new token with email as sub
    access_token = create_access_token(data={"sub":user.email}, delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me", response_model=UserOut)
def read_users_me(current_user: Annotated[UserOut, Depends(get_current_user)])->UserOut:
    return UserOut(username=current_user.username, date=current_user.date)

@app.post("/user/note", response_model=NewNote)
def post_new_note(body: NewNoteIn,
                   db: Annotated[Session, Depends(init_db)],
                   current_user: Annotated[User, Depends(get_current_user)]) -> NewNote:
    if not body or not body.data:
        raise HTTPException(status_code=401, detail="invalid data, please add content to note")
    newNote = create_new_note(content=body.data, user=current_user, db=db)
    return newNote

@app.get("/user/notes", response_model=NoteOut)
def get_user_notes(db: Annotated[Session, Depends(init_db)],
                    current_user: Annotated[User, Depends(get_current_user)]) -> NoteOut:
    return _get_user_notes(db=db, user=current_user)

@app.put("/user/note/{id}")
def update_note(db: Annotated[Session, Depends(init_db)], currentUser: Annotated[User, Depends(get_current_user)], id: int, data: str):
    result = edit_note(data=data, id=id, db=db)
    return result

@app.delete("/user/note/{id}")
def _delete_note(db: Annotated[Session, Depends(init_db)], currentUser: Annotated[User, Depends(get_current_user)], id: int):
    result = delete_note(db=db, id=id)
    if result:
        return {"Note deleted successfully": result}
    else:
        raise HTTPException(status_code=404, detail="Note not found")



if __name__ == "__main__":
    pass
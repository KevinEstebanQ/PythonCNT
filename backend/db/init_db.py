from .session_maker import SessionLocal

def init_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
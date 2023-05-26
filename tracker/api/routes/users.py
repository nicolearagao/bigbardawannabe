from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from tracker.schemas.schemas import UserSchema
from tracker.db.models.user import User
from tracker.db.session import get_db

router = APIRouter()

@router.post("/", response_model=list[UserSchema])
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users
from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound,NoResultFound
from typing import List

from tracker.schemas.schemas import UserSchema, UserOptional
from tracker.db.models.user import User
from tracker.db.session import get_db

router = APIRouter()

@router.post("/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.username == user.username).one_or_none()
    except MultipleResultsFound:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Multiple users with the same username found."
        )
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_existing_user(db: Session, username: str) -> bool:
    existing_user = db.query(User).filter(User.username == username).one_or_none()
    return existing_user is not None

def create_user(user: UserSchema, db: Session) -> User:
    if check_existing_user(db, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")

    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/", response_model=UserSchema)
def create_user_endpoint(user: UserSchema, db: Session = Depends(get_db)):
    try:
        return create_user(user, db)
    except MultipleResultsFound:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Multiple users with the same username found."
        )


@router.get("/", response_model=List[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.delete("/")
def delete_all_users(db: Session = Depends(get_db)):
    db.query(User).delete()
    db.commit()
    return {"message": "All users deleted"}


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", response_model=UserSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user


@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, updated_user: UserOptional, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in updated_user.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

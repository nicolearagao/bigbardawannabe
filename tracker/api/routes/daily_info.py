from datetime import date, datetime

from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List

from tracker.schemas.schemas import DailyInfoSchema
from tracker.db.models.daily_info import DailyInfo
from tracker.db.models.user import User
from tracker.db.session import get_db

router = APIRouter()

@router.post("/{user_id}/daily_info", response_model=DailyInfoSchema)
def create_daily_for_user(user_id: int, daily: DailyInfoSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    daily.user_id = user_id
    if not user:
        raise HTTPException(status_code=404, detail="You must provide a valid user.")
    db_daily = DailyInfo(**daily.dict())
    db.add(db_daily)
    db.commit()
    db.refresh(db_daily)
    return db_daily


@router.get("/{user_id}/daily_info", response_model=List[DailyInfoSchema])
def get_daily_info_filter_by_period(user_id: int, start_date: date = None, end_date: date = None, db: Session = Depends(get_db)):
    query = db.query(DailyInfo).filter(DailyInfo.user_id == user_id)
    if start_date:
        query = query.filter(func.DATE(DailyInfo.created_at) >= start_date)
    if end_date:
        query = query.filter(func.DATE(DailyInfo.created_at) <= end_date)
    daily_infos = query.all()
    if not daily_infos:
        raise HTTPException(status_code=404, detail="This user hasn't created any daily info in the selected period.")
    return daily_infos


@router.get("/{user_id}/daily_info", response_model=List[DailyInfoSchema])
def get_daily_info_by_user(user_id: int, db: Session = Depends(get_db)):
    daily_infos = db.query(DailyInfo).filter(DailyInfo.user_id == user_id).all()
    if not daily_infos:
        raise HTTPException(status_code=404, detail="This user hasn't created any daily infos yet")
    return daily_infos


@router.delete("/{user_id}/daily_info/{daily_id}", response_model=DailyInfoSchema)
def delete_daily(user_id: int, daily_id: int, db: Session = Depends(get_db)):
    user = db.query(DailyInfo).filter(DailyInfo.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    daily_info = db.query(DailyInfo).filter(DailyInfo.user_id == user_id, DailyInfo.id == daily_id).first()
    if not daily_info:
        raise HTTPException(status_code=404, detail="Daily not found")
    db.delete(daily_info)
    db.commit()
    return user


@router.put("/{user_id}/daily_info/{daily_id}", response_model=DailyInfoSchema)
def update_daily_info(user_id: int, daily_id: int, updated_info: DailyInfoSchema, db: Session = Depends(get_db)):
    user = db.query(DailyInfo).filter(DailyInfo.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    daily_info = db.query(DailyInfo).filter(DailyInfo.user_id == user_id, DailyInfo.id == daily_id).first()
    if not daily_info:
        raise HTTPException(status_code=404, detail="Daily not found")
    for field, value in updated_info.dict(exclude_unset=True).items():
        setattr(daily_info, field, value)
    db.commit()
    db.refresh(daily_info)
    return daily_info

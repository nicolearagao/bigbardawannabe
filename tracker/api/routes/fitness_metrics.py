from datetime import date, datetime

from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List

from tracker.schemas.schemas import FitnessMetricsSchema
from tracker.db.models.fitness_metrics import FitnessMetrics
from tracker.db.models.user import User
from tracker.db.session import get_db

router = APIRouter()

@router.post("/{user_id}/metrics", response_model=FitnessMetricsSchema)
def create_metrics_for_user(user_id: int, metrics: FitnessMetricsSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    metrics.user_id = user_id
    if not user:
        raise HTTPException(status_code=404, detail="You must provide a valid user.")
    existing_metrics = db.query(FitnessMetrics).filter(FitnessMetrics.user_id == user_id).first()
    if existing_metrics:
        raise HTTPException(status_code=400, detail="Fitness metrics already exist for this user.")

    db_metrics = FitnessMetrics(**metrics.dict())
    db.add(db_metrics)
    db.commit()
    db.refresh(db_metrics)
    return db_metrics


@router.get("/{user_id}/metrics", response_model=FitnessMetricsSchema)
def get_user_metrics(user_id: int, db: Session = Depends(get_db)):
    metrics = db.query(FitnessMetrics).filter(FitnessMetrics.user_id == user_id).first()
    if not metrics:
        raise HTTPException(status_code=404, detail="Metrics not found")
    return metrics


@router.delete("/{user_id}/metrics")
def delete_metrics(user_id: int, db: Session = Depends(get_db)):
    user = db.query(FitnessMetrics).filter(FitnessMetrics.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    metrics = db.query(FitnessMetrics).filter(FitnessMetrics.user_id == user_id).first()
    if not metrics:
        raise HTTPException(status_code=404, detail="Metrics not found")
    db.delete(metrics)
    db.commit()
    return {"msg": "Metrics were successfully deleted"}


# @router.put("/{user_id}/daily_info/{daily_id}", response_model=DailyInfoSchema)
# def update_daily_info(user_id: int, daily_id: int, updated_info: DailyInfoSchema, db: Session = Depends(get_db)):
#     user = db.query(DailyInfo).filter(DailyInfo.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     daily_info = db.query(DailyInfo).filter(DailyInfo.user_id == user_id, DailyInfo.id == daily_id).first()
#     if not daily_info:
#         raise HTTPException(status_code=404, detail="Daily not found")
#     for field, value in updated_info.dict(exclude_unset=True).items():
#         setattr(daily_info, field, value)
#     db.commit()
#     db.refresh(daily_info)
#     return daily_info

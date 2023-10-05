from sqlalchemy import Column, ForeignKey, Integer, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base


class StrengthTraining(Base, BaseMixin):
    __tablename__ = "strength_training"

    daily_info_id = Column(Integer, ForeignKey("daily_info.id"), nullable=False)
    length = Column(Integer)
    accessory_exercises = Column(Boolean)

    daily_info = relationship("DailyInfo", uselist=False, backref="strength_training")

    __table_args__ = (UniqueConstraint("daily_info_id"),)

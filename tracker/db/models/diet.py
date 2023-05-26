from sqlalchemy import Column, ForeignKey, Integer, Boolean, Enum
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base
from tracker.schemas.enumerators import CheatMealType


class Diet(Base, BaseMixin):
    __tablename__ = "diet"

    daily_info_id = Column(Integer, ForeignKey("daily_info.id"), nullable=False)
    adherence_percentage = Column(Integer)
    cheat_meal = Column(Boolean)
    cheat_meal_type = Column(Enum(CheatMealType), nullable=True)

    daily_info = relationship("DailyInfo", uselist=False, backref="diet")


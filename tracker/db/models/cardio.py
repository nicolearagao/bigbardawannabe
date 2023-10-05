from sqlalchemy import Column, ForeignKey, Integer, Enum, UniqueConstraint
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base
from tracker.schemas.enumerators import CardioType


class Cardio(Base, BaseMixin):
    __tablename__ = "cardio"

    daily_info_id = Column(Integer, ForeignKey("daily_info.id"), nullable=False)
    length = Column(Integer)
    type = Column(Enum(CardioType))

    daily_info = relationship("DailyInfo", uselist=False, backref="cardio")

    __table_args__ = (UniqueConstraint("daily_info_id"),)

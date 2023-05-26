from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base


class DailyInfo(Base, BaseMixin):
    __tablename__ = "daily_info"

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    water_intake = Column(Float)

    user = relationship("User", backref="daily_info")

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base


class FitnessMetrics(Base, BaseMixin):
    __tablename__ = "fitness_metrics"

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    weight = Column(Float)
    weight_goal = Column(Float)
    height = Column(Float)
    fat_percentage = Column(Integer)
    calorie_intake = Column(Integer)

    user = relationship("User", uselist=False, backref="fitness_metrics")

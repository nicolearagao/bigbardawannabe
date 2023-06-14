from sqlalchemy import Column, Float, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base


class FitnessMetrics(Base, BaseMixin):
    __tablename__ = "fitness_metrics"

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    weight = Column(Float, nullable=True, default=None)
    weight_goal = Column(Float, nullable=True, default=None)
    height = Column(Float, nullable=True, default=None)
    fat_percentage = Column(Integer, nullable=True, default=None)
    calorie_intake = Column(Integer, nullable=True, default=None)

    user = relationship("User", uselist=False, backref="fitness_metrics")

    __table_args__ = (UniqueConstraint("user_id"))

from sqlalchemy import Column, Float, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base
from tracker.schemas.enumerators import SBD


class Single(Base, BaseMixin):
    __tablename__ = "single"

    strength_training_id = Column(Integer, ForeignKey("strength_training.id"), nullable=False)
    session_weight = Column(Float)
    type = Column(Enum(SBD))

    strength_training = relationship("StrengthTraining", backref="single")

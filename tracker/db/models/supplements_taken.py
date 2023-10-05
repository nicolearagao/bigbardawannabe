from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, UniqueConstraint
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base


class SupplementsTaken(Base, BaseMixin):
    __tablename__ = "supplements_taken"

    was_taken = Column(Boolean)
    supplement_type = Column(String)
    diet_id = Column(Integer, ForeignKey("diet.id"), nullable=False)

    diet = relationship("Diet", backref="supplements_taken")

    __table_args__ = (UniqueConstraint("diet_id"),)

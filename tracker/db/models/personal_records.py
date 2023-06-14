from sqlalchemy import Column, Float, ForeignKey, Enum, DateTime, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.schemas.enumerators import SBD, PersonalRecordType
from tracker.db.session import Base


class PersonalRecords(Base, BaseMixin):
    __tablename__ = "personal_records"

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    type = Column(Enum(PersonalRecordType))
    lift = Column(Enum(SBD))
    date = Column(DateTime, nullable=False)
    weight = Column(Float)

    user = relationship("User", backref="personal_records")

    __table_args__ = (UniqueConstraint("user_id"))

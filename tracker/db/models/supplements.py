from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from tracker.db.base import BaseMixin
from tracker.db.session import Base


class Supplement(Base, BaseMixin):
    __tablename__ = "supplement"

    type = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", backref="supplement")

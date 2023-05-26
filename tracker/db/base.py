from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base

class BaseMixin:
    """A mixin class that gathers the default columns for any models."""

    __name__ = "BaseMixin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)


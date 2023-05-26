from datetime import datetime
from pydantic import BaseModel, Field

class Base(BaseModel):
    id: int = Field(description="Unique identifier", default=None)
    created_at: datetime = Field(description="creation timestamp", default=None)

    class Config:
        orm_mode = True

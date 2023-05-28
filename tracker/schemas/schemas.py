import re
from datetime import datetime

from pydantic import validator, Field
<<<<<<< HEAD
<<<<<<< HEAD
from typing import List
=======
from typing import Optional
>>>>>>> 143f78d (fixup! feature(schemas): add schemas folder)
=======
from typing import List, Optional
>>>>>>> 7ba629e (feature(routes): add user)

from tracker.schemas.base import Base
from tracker.schemas.enumerators import CardioType, CheatMealType, SBD, PersonalRecordType


class UserSchema(Base):
    username: str
    password: str

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 8 or not re.search(r"\d", value):
            raise ValueError("Password must contain at least 8 characters and a number.")
        return value

class UserOptional(UserSchema):
    __annotations__ = {k: Optional[v] for k, v in UserSchema.__annotations__.items()}


class DailyInfoSchema(Base):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)
    user_id: int = Field(description="Foreign key referencing the User table")
    water_intake: float # todo implement warning which will calculate minimum amount of water needed per day looking at weight, height and exercise

    @validator("water_intake")
    def validate_water_intake(cls, value):
        if value < 0:
            raise ValueError("Water intake must be greater than or equal to zero.")
        return value


class Cardio(Base):
    length: int 
    type: CardioType
    daily_info_id: int = Field(description="Foreign key referencing the DailyInfo table")

    @validator("length")
    def validate_cardio_length(cls, value):
        if value < 0:
            raise ValueError("Cardio length must be greater than or equal to zero.")
        return value


class StrengthTraining(Base):
    daily_info_id: int = Field(description="Foreign key referencing the DailyInfo table")
    length: int 
    accessory_exercises: bool

    @validator("length")
    def validate_training_length(cls, value):
        if value < 0:
            raise ValueError("Training length must be greater than or equal to zero.")
        return value


class Supplement(Base):
    type: str
    user_id: int = Field("Foreign key referencing the User table")


class SupplementsTaken(Base):
    id: int = Field(default=None)
    created_at: datetime = Field(default=None)    
    supplement_type: Supplement
    was_taken: bool


class Diet(Base):
    daily_info_id: int = Field(description="Foreign key referencing the DailyInfo table")
    adherence_percentage: int
    cheat_meal: bool
    cheat_meal_type: CheatMealType


class Single(Base):
    strength_training_id: int = Field(description="Foreign key referencing the StrengthTraining table")
    type: SBD
    session_weight: float


class FitnessMetrics(Base):
    user_id: int = Field("Foreign key referencing the User table")
    weight: float
    height: float
    fat_percentage: int
    weight_goal: float
    calorie_intake: int # todo implement validator which will look to height and weight and will calculate minimum amount of calories needed 

    @validator("weight", "weight_goal", "height", "calorie_intake")
    def validate_positive_value(cls, value):
        if value <= 0:
            raise ValueError("Value must be a positive number.")
        return value
    
    @validator("fat_percentage")
    def validate_fat_percentage(cls, value):
        if value < 0 or value > 100:
            raise ValueError("Fat percentage must be between 0 and 100.")
        return value


class PersonalRecords(Base):
    user_id: int = Field(description="Foreign key referencing the User table")
    type: PersonalRecordType
    lift: SBD
    date: datetime
    weight: float

# todo add tests

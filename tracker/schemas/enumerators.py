from enum import Enum

class CardioType(str, Enum):
    WALKING = "Walking"
    CYCLING = "Cycling"
    SWIMMING = "Swimming"
    TRANSPORT = "Transport"
    OTHER = "Other"


class CheatMealType(str, Enum):
    BURGUER = "burguer"
    PIZZA = "pizza"
    JAPANESE = "japanese"
    BRUNCH = "brunch"
    GERMAN = "german"
    CHINESE = "chinese"
    KEBAB = "kebab"
    ITALIAN = "italian"
    POPCORN = "popcorn"
    SWEETS = "sweets"


class SBD(str, Enum):
    SQUAT = "squat"
    BENCH = "bench press"
    DEADLIFT = "deadlift"


class PersonalRecordType(str, Enum):
    MEET = "meet"
    TRAINING = "training"


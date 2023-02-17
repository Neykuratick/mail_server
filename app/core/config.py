from enum import Enum

from pydantic import BaseSettings
from pydantic import Field


class TimeMeasurementUnits(str, Enum):
    days = "days"
    seconds = "seconds"
    microseconds = "microseconds"
    milliseconds = "milliseconds"
    minutes = "minutes"
    hours = "hours"
    weeks = "weeks"


class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: list[str] = Field(default=["*"])
    API_V1_URL: str = Field(default="/api")
    JWT_SECRET: str = Field(default="change_me")
    JWT_ALGORITHM: str = Field(default="HS256")
    SECRET_EXPIRATION_TIME: int = Field(default=1)
    SECRET_MEASUREMENT_UNIT: TimeMeasurementUnits = Field(default=TimeMeasurementUnits.days)


settings = Settings()

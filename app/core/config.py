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
    APP_TITLE: str = Field(default="Mail Server")

    BACKEND_CORS_ORIGINS: list[str] = Field(default=["*"])
    API_V1_URL: str = Field(default="/api")
    DEBUG: bool = Field(default=True)

    ADMIN_SECRET_KEY = Field(default="root")

    JWT_SECRET: str = Field(default="change_me")
    JWT_ALGORITHM: str = Field(default="HS256")
    SECRET_EXPIRATION_TIME: int = Field(default=5)
    SECRET_MEASUREMENT_UNIT: TimeMeasurementUnits = Field(default=TimeMeasurementUnits.days)

    POSTGRES_USER: str = Field(default="root")
    POSTGRES_PASSWORD: str = Field(default="root")
    POSTGRES_SERVER: str = Field(default="localhost")
    POSTGRES_PORT: str = Field(default="5432")
    POSTGRES_DB: str = Field(default="db")

    @property
    def POSTGRES_URL(self):
        return "postgresql://{}:{}@{}/{}".format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_SERVER,
            self.POSTGRES_DB,
        )

    @property
    def POSTGRES_URL_ASYNC(self):
        return "postgresql+asyncpg://{}:{}@{}/{}".format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_SERVER,
            self.POSTGRES_DB,
        )


settings = Settings()

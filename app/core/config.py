from pydantic import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: list[str] = Field(default=['*'])


settings = Settings()

from typing import TypeVar

from pydantic import BaseModel as BaseModelPydantic
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData

metadata = MetaData()
Base = declarative_base(metadata=metadata)

BaseModelType = TypeVar("BaseModelType", bound=Base)


class BaseScheme(BaseModelPydantic):
    class Config:
        orm_mode = True

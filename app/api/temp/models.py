from sqlalchemy import Column, Integer, String
from app.db import Base


class Temp(Base):
    __tablename__ = "temp"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

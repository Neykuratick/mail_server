from app.db.base_model import BaseModel


class UserReadScheme(BaseModel):
    id: int
    username: str
    email: str


class UserCreateScheme(BaseModel):
    username: str
    email: str
    password: str

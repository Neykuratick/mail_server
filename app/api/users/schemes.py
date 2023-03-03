from app.db.base_model import BaseScheme


class UserReadScheme(BaseScheme):
    id: int
    username: str
    email: str


class UserCreateScheme(BaseScheme):
    username: str
    email: str
    password: str

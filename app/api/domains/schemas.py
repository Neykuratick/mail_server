from app.api.users.schemes import UserReadScheme
from app.db.base_model import BaseModel


class DomainCreateScheme(BaseModel):
    name: str


class DomainReadScheme(BaseModel):
    id: int
    name: str
    owner: UserReadScheme


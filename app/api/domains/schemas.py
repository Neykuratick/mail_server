from app.api.domains.models import DomainModel
from app.api.users.schemes import UserReadScheme
from app.db.base_model import BaseScheme


class DomainCreateScheme(BaseScheme):
    name: str


class DomainReadScheme(BaseScheme):
    id: int
    name: str
    owner: UserReadScheme

    class Meta:
        orm_model = DomainModel

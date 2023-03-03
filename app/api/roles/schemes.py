from app.db.base_model import BaseScheme


class RoleScheme(BaseScheme):
    id: int
    name: str
    human_name: str
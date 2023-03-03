from app.api.permissions.enums import ActionsEnum
from app.api.permissions.enums import TargetsEnum
from app.db.base_model import BaseScheme


class TargetScheme(BaseScheme):
    id: int
    name: TargetsEnum
    human_name: str


class ActionScheme(BaseScheme):
    id: int
    name: ActionsEnum
    human_name: str


class PermissionScheme(BaseScheme):
    id: int
    target: TargetScheme
    action: ActionScheme

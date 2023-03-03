from app.api.permissions.models import PermissionActionModel
from app.api.permissions.models import PermissionTargetModel
from app.api.permissions.models import PermissionTargetsActions
from app.core.admin_core import ModelView


class PermissionTargetsAdmin(ModelView, model=PermissionTargetModel):
    column_list = [
        PermissionTargetModel.id,
        PermissionTargetModel.name,
        PermissionTargetModel.human_name,
    ]


class PermissionActionsAdmin(ModelView, model=PermissionActionModel):
    column_list = [
        PermissionActionModel.id,
        PermissionActionModel.name,
        PermissionActionModel.human_name,
    ]


class PermissionTargetsActionsAdmin(ModelView, model=PermissionTargetsActions):
    column_list = [PermissionActionModel.id]

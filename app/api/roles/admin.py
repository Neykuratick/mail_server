from app.api.roles.models import RoleModel
from app.api.roles.models import RolesTargetActions
from app.core.admin_core import ModelView


class RolesAdmin(ModelView, model=RoleModel):
    column_list = [RoleModel.id, RoleModel.name, RoleModel.human_name]


class RolesTargetActionsAdmin(ModelView, model=RolesTargetActions):
    column_list = [RolesTargetActions.id]

from app.api.roles.models import Roles
from app.api.roles.models import RolesTargetActions
from app.core.admin_core import ModelView


class RolesAdmin(ModelView, model=Roles):
    column_list = [Roles.id, Roles.name, Roles.human_name]


class RolesTargetActionsAdmin(ModelView, model=RolesTargetActions):
    column_list = [RolesTargetActions.id]
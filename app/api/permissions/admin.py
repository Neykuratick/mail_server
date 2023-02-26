from app.api.permissions.models import PermissionActions
from app.api.permissions.models import PermissionTargets
from app.api.permissions.models import PermissionTargetsActions
from app.core.admin_core import ModelView


class PermissionTargetsAdmin(ModelView, model=PermissionTargets):
    column_list = [PermissionTargets.id, PermissionTargets.name, PermissionTargets.human_name]


class PermissionActionsAdmin(ModelView, model=PermissionActions):
    column_list = [PermissionActions.id, PermissionActions.name, PermissionActions.human_name]


class PermissionTargetsActionsAdmin(ModelView, model=PermissionTargetsActions):
    column_list = [PermissionActions.id]

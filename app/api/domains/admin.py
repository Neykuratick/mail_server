from app.api.domains.models import DomainModel
from app.api.users.models import UserModel
from app.core.admin_core import ModelView


class ModelAdmin(ModelView, model=DomainModel):
    column_list = [DomainModel.id, DomainModel.name]

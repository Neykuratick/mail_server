from app.api.domains.models import DomainModel
from app.core.admin_core import ModelView


class DomainAdmin(ModelView, model=DomainModel):
    column_list = [DomainModel.id, DomainModel.name]

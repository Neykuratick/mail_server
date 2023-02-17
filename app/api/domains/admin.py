from sqladmin import ModelView

from app.api.domains.models import DomainModel


class ModelAdmin(ModelView, model=DomainModel):
    column_list = [DomainModel.id, DomainModel.name]

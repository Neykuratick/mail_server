from sqladmin import ModelView

from app.api.users.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]

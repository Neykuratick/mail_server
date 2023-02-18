from app.api.users.models import UserModel
from app.core.admin_core import ModelView


class UserAdmin(ModelView, model=UserModel):
    column_list = [UserModel.id, UserModel.username]
    form_widget_args = ModelView.form_widget_args | dict(hashed_password=dict(readonly=True))

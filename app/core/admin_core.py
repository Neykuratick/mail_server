from sqladmin import ModelView as BaseModelView


class ModelView(BaseModelView):
    save_as = True
    form_widget_args = dict(created_at=dict(readonly=True))

from sqladmin import ModelView as BaseModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from app.api.security.deps import validate_decode_token
from app.api.security.service import authenticate
from app.api.users.crud import UsersCRUD
from app.db.dep import async_session


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        body = await request.body()
        params = body.decode("utf-8").split("&")
        username, password = params[0].split("=")[1], params[1].split("=")[1]

        async with async_session() as session:
            users_crud = UsersCRUD(session=session)
            token = await authenticate(username=username, password=password, users=users_crud)

        request.session.update({"token": token.access_token})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        try:
            payload = validate_decode_token(token=token)
        except Exception as e:
            request.session.clear()
            raise e

        return True


class ModelView(BaseModelView):
    save_as = True
    form_widget_args = dict(created_at=dict(readonly=True))

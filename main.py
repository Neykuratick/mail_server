from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from app.api.dispatcher import admin_views
from app.api.dispatcher import api_router
from app.core.admin_core import AdminAuth
from app.core.config import settings
from app.db.dep import engine

app = FastAPI()
admin_auth = AdminAuth(secret_key=settings.ADMIN_SECRET_KEY)

admin = Admin(
    app=app,
    engine=engine,
    base_url="/admin",
    title=f"{settings.APP_TITLE} Administration",
    debug=settings.DEBUG,
    authentication_backend=admin_auth,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


for view in admin_views:
    admin.add_view(view)

from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from app.api.dispatcher import admin_views
from app.api.dispatcher import api_router
from app.core.config import settings
from app.db.dep import engine

app = FastAPI()
app.openapi_url
admin = Admin(app, engine)

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

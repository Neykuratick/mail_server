from pydantic import Field

from app.db.base_model import BaseScheme


class TokenScheme(BaseScheme):
    access_token: str = Field(...)
    token_type: str = Field(default="bearer")

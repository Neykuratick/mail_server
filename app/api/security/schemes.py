from pydantic import Field

from app.db.base_model import BaseModel


class TokenScheme(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(default='bearer')
    
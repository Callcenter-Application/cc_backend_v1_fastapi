from datetime import datetime

from sqlmodel import SQLModel, Field


class RevokedToken(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    jti: str = Field(unique=True, index=True)
    expires_at: datetime

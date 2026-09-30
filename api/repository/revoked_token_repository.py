from datetime import datetime

from sqlmodel import Session, select

from api.models.revoked_token_model import RevokedToken


class RevokedTokenRepository:

    def add(self, jti: str, expires_at: datetime, session: Session) -> RevokedToken:
        revoked_token = RevokedToken(jti=jti, expires_at=expires_at)
        session.add(revoked_token)
        session.commit()
        session.refresh(revoked_token)
        return revoked_token

    def exists(self, jti: str, session: Session) -> bool:
        statement = select(RevokedToken).where(RevokedToken.jti == jti)
        return session.exec(statement).one_or_none() is not None

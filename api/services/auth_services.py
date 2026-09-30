from datetime import datetime, timezone

from api.repository.auth_repository import AuthRepository
from api.repository.revoked_token_repository import RevokedTokenRepository
from api.utils.passhass import PasswordHasher
from api.utils.jwt_util import JWTUtil


class AuthServices:
    def __init__(self):
        self._auth_repository = AuthRepository()
        self._revoked_token_repository = RevokedTokenRepository()
        self._password_hasher = PasswordHasher()
        self._jwt_util = JWTUtil()

    def login(self, email, password, session):
        user = self._auth_repository.find_one(email, session)
        if user and self._password_hasher.verify(password, user.password):
            token = self._jwt_util.generate_token({"sub": str(user.id), "email": user.email})
            return user, token
        return None, None

    def logout(self, payload: dict, session) -> dict:
        jti = payload.get("jti")
        exp = payload.get("exp")
        if not jti or not exp:
            raise ValueError("Token is missing required claims for revocation")

        expires_at = datetime.fromtimestamp(exp, tz=timezone.utc)
        self._revoked_token_repository.add(jti, expires_at, session)
        return {"message": "Token invalidated"}

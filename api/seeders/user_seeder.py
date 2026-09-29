from sqlmodel import Session, select
from api.models.user_model import User
from api.models.role_model import Role
from api.utils.passhass import PasswordHasher

DEFAULT_USERS = [
    {"name": "Admin", "email": "admin@example.com", "password": "Admin1234@", "role_name": "admin"},
    {"name": "Operator", "email": "operator@example.com", "password": "Operator1234@", "role_name": "operator"},
    {"name": "Supervisor", "email": "supervisor@example.com", "password": "Supervisor1234@", "role_name": "supervisor"},
]

_password_hasher = PasswordHasher()


def seed_users(session: Session) -> None:
    for data in DEFAULT_USERS:
        exists = session.exec(select(User).where(User.email == data["email"])).one_or_none()
        if exists:
            continue

        role = session.exec(select(Role).where(Role.name == data["role_name"])).one_or_none()
        if role is None or role.id is None:
            continue

        session.add(User(
            name=data["name"],
            email=data["email"],
            password=_password_hasher.generate_hash(data["password"]),
            role_id=role.id 
        ))
    session.commit()

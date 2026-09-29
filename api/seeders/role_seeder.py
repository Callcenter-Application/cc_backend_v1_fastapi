from sqlmodel import Session, select
from api.models.role_model import Role

DEFAULT_ROLES = ["admin", "operator", "supervisor"]


def seed_roles(session: Session) -> None:
    for name in DEFAULT_ROLES:
        exists = session.exec(select(Role).where(Role.name == name)).one_or_none()
        if not exists:
            session.add(Role(name=name))
    session.commit()

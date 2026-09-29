from sqlmodel import Session
from api.config.db import engine, create_db_and_tables
from api.seeders.role_seeder import seed_roles
from api.seeders.user_seeder import seed_users


def run_seeders() -> None:
    create_db_and_tables()
    with Session(engine) as session:
        seed_roles(session)
        seed_users(session)


if __name__ == "__main__":
    run_seeders()

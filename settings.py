import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)


class DatabaseConfiguration:
    project_name: str = "TodoAPI + Postgres"
    project_version: str = "Version 1.1.0"

    Postgres_user:      str = os.getenv("POSTGRES_USER")
    Postgres_pass:      str = os.getenv("POSTGRES_PASS")
    Postgres_server:    str = os.getenv("POSTGRES_SERVER")
    Postgres_port:      str = os.getenv("POSTGRES_PORT")
    Postgres_database:  str = os.getenv("POSTGRES_DATABASE")
    Database_url = f'postgresql://{Postgres_user}:{Postgres_pass}' \
                   f'@{Postgres_server}:{Postgres_port}/{Postgres_database}'


settings = DatabaseConfiguration()

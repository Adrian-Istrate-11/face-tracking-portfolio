import os
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import Session, sessionmaker, declarative_base

from config import DBNAME  # fara 'src.'

load_dotenv()

SQL_Base = declarative_base()


def generate_sql_url() -> str:
    # 1) Render / production: DATABASE_URL (cel mai simplu)
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        # SQLAlchemy vrea driver explicit
        url = db_url.replace("postgresql://", "postgresql+psycopg2://", 1)

        # Render Postgres cere de obicei SSL
        if "sslmode=" not in url:
            sep = "&" if "?" in url else "?"
            url = f"{url}{sep}sslmode=require"

        return url

    # 2) Local fallback: din variabile separate
    drivers = os.getenv("SQL_DRIVERS", "postgresql+psycopg2")
    host = os.getenv("SQL_HOST", "localhost")
    port = os.getenv("SQL_PORT", "5432")
    dbname = os.getenv("SQL_DBNAME", DBNAME)
    user = os.getenv("SQL_USER", "postgres")
    password = os.getenv("SQL_PASSWORD", "")

    return f"{drivers}://{user}:{password}@{host}:{port}/{dbname}"


SQL_URL = generate_sql_url()
SQL_ENGINE = sqlalchemy.create_engine(SQL_URL, pool_pre_ping=True)
_SQL_SESSIONMAKER = sessionmaker(bind=SQL_ENGINE)


class SQLSesssion:
    def __init__(self):
        self._session = _SQL_SESSIONMAKER()

    def __enter__(self) -> Session:
        return self._session

    def __exit__(self, *_) -> None:
        self._session.close()

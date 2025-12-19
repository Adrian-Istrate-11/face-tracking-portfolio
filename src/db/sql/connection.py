import os
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import Session, sessionmaker, declarative_base

from config import DBNAME  # fara 'src.'

load_dotenv()

SQL_DRIVERS = os.getenv("SQL_DRIVERS", "mysql+pymysql")
SQL_HOST = os.getenv("SQL_HOST", "localhost")
SQL_PORT = os.getenv("SQL_PORT", "")  # optional
SQL_DBNAME = os.getenv("SQL_DBNAME", DBNAME)
SQL_USER = os.getenv("SQL_USER", "root")
SQL_PASSWORD = os.getenv("SQL_PASSWORD", "1117")


def generate_sql_url() -> str:
    port_part = f":{SQL_PORT}" if SQL_PORT else ""
    return f"{SQL_DRIVERS}://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}{port_part}/{SQL_DBNAME}"


SQL_URL = generate_sql_url()
SQL_ENGINE = sqlalchemy.create_engine(SQL_URL, pool_pre_ping=True)
_SQL_SESSIONMAKER = sessionmaker(bind=SQL_ENGINE)

SQL_Base = declarative_base()


class SQLSesssion:
    def __init__(self):
        self._session = _SQL_SESSIONMAKER()

    def __enter__(self) -> Session:
        return self._session

    def __exit__(self, *_) -> None:
        self._session.close()

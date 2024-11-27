import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker
#from typing import Generator
from src.config import DBNAME

#Load enviroments variables from .env file
load_dotenv()


SQL_DRIVERS = "mysql+pymysql"
SQL_HOST = "localhost"
SQL_DBNAME = DBNAME

def generate_sql_url() -> str:
    """
    Create the SQL DB URL for sqlalchemy
    """
    user = os.getenv("SQL_USER", "root")
    passwd = os.getenv("SQL_PASSWORD", "adolf")
    return f"{SQL_DRIVERS}://{user}:{passwd}@{SQL_HOST}/{SQL_DBNAME}"

SQL_URL = generate_sql_url()
SQL_ENGINE = sqlalchemy.create_engine(SQL_URL)

_SQL_SESSIONMAKER = sessionmaker(bind=SQL_ENGINE)

class SQLSesssion:

    def __init__(self):
        self._session = _SQL_SESSIONMAKER()

    def __enter__(self) -> Session:
        return self._session

    def __exit__(self, *_) -> None:
        self._session.close()
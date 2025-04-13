import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from config import DBNAME  # Fără 'src.'

# Încarcă variabilele din .env dacă există
load_dotenv()

# Variabile de conectare
SQL_DRIVERS = "mysql+pymysql"
SQL_HOST = "localhost"
SQL_DBNAME = DBNAME

# Creează URL-ul DB
def generate_sql_url() -> str:
    user = os.getenv("SQL_USER", "root")
    passwd = os.getenv("SQL_PASSWORD", "1117")
    return f"{SQL_DRIVERS}://{user}:{passwd}@{SQL_HOST}/{SQL_DBNAME}"

# Creează engine și session maker
SQL_URL = generate_sql_url()
SQL_ENGINE = sqlalchemy.create_engine(SQL_URL)
_SQL_SESSIONMAKER = sessionmaker(bind=SQL_ENGINE)

# Declarative base pentru toate modelele
SQL_Base = declarative_base()

class SQLSesssion:
    def __init__(self):
        self._session = _SQL_SESSIONMAKER()

    def __enter__(self) -> Session:
        return self._session

    def __exit__(self, *_) -> None:
        self._session.close()

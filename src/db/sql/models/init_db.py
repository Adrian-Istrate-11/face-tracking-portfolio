from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .sql_base import SQL_Base  # Importă SQL_Base
from .employee import Employee  # Import corect pentru Employee
from .maintenance import Maintenance
from .person import Person
from .visitors import Visitors
from src.db.sql.connection import generate_sql_url

DATABASE_URL=generate_sql_url()

#DATABASE_URL = "mysql+pymysql://Andreea:<password>@localhost:3306/<database_name>"

#DATABASE_URL = "mysql+mysqlconnector://root:adolf@localhost:3306/face_tracking"
#DATABASE_URL = "mysql+pymysql://Andreea:<password>@localhost:3306/<database_name>"

# Crearea motorului de bază de date
engine = create_engine(DATABASE_URL, echo=True)

# Creează sesiunea
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Creează tabelele definite în toate modelele
    SQL_Base.metadata.create_all(bind=engine)
    print("Tabelele au fost create cu succes.")



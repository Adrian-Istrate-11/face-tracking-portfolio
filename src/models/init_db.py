from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .sql_base import SQL_Base  # Importă SQL_Base
from .employee import Employee  # Import corect pentru Employee
from .maintenance import Maintenance
from .person import Person
from .visitors import Visitors

DATABASE_URL = "mysql+mysqlconnector://root:adolf@localhost:3306/face_tracking"

# Crearea motorului de bază de date
engine = create_engine(DATABASE_URL, echo=True)

# Creează sesiunea
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Creează tabelele definite în toate modelele
    SQL_Base.metadata.create_all(bind=engine)
    print("Tabelele au fost create cu succes.")



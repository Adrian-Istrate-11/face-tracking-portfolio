from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.sql.connection import generate_sql_url
from db.sql.models import SQL_Base  # Declarativ base
from db.sql.models import Person, Employee, Maintenance, Visitors  # Modelele tale

# Generează URL-ul de conectare din variabilele de mediu sau fallback
DATABASE_URL = generate_sql_url()

# Creează motorul de conectare SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Creează sesiunea de lucru cu baza de date
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Funcția care inițializează baza de date
def init_db():
    SQL_Base.metadata.create_all(bind=engine)
    print("Tabelele au fost create cu succes.")


#Apeleaza funcția direct când rulezi scriptul
if __name__ == "__main__":
    init_db()

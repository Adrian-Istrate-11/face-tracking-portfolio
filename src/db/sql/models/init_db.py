from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.sql.connection import generate_sql_url
from db.sql.models import SQL_Base
from db.sql.models import Person, Employee, Maintenance, Visitors

# Generează URL-ul DB din variabilele de mediu
DATABASE_URL = generate_sql_url()

# Creează motorul SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Creează sesiunea de lucru
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Funcția care creează tabelele
def init_db():
    SQL_Base.metadata.create_all(bind=engine)
    print("Tabelele au fost create cu succes.")


# Execută funcția dacă rulăm direct acest fișier
if __name__ == "__main__":
    init_db()




import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from db.sql.connection import SQLSesssion
from sqlalchemy import text

try:
    with SQLSesssion() as session:
        session.execute(text("SELECT 1"))
    print("Conexiune reușită la baza de date!")
except Exception as e:
    print("Eroare la conectare:", e)


import sys
import os

# Adaugă calea absolută a directorului `src` la calea de import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from db.sql.models.init_db import init_db  # Importul corect al funcției init_db

if __name__ == "__main__":
    init_db()  # Apelează funcția pentru a crea tabelele în baza de date
    print("Tabelele au fost create cu succes.")








#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.db.sql.init_db import init_sql_db

if __name__ == "__main__":
    print("Initialiazing SQL database")
    init_sql_db()

from sqlalchemy import Column, Integer, String
from .sql_base import SQL_Base
from sqlalchemy import Time  # Dacă orele sunt tratate ca timp

class Maintenance(SQL_Base):
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)  # Aici specificăm o lungime de 50 pentru numele mentenanței
    start_hour = Column(Integer, nullable=False, default=21)  # Păstrăm start_hour ca Integer, fără dimensiune
    end_hour = Column(Integer, nullable=False, default=4)  # Păstrăm end_hour ca Integer, fără dimensiune






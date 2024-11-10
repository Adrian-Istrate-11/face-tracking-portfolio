from sqlalchemy import Column, Integer, String
from .sql_base import SQL_Base

class Person(SQL_Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    person_name = Column(String(100), nullable=False)  # Am adăugat 100 de caractere pentru numele persoanei
    person_type = Column(String(50), nullable=False)   # Am adăugat 50 de caractere pentru tipul persoanei
    entry_time = Column(Integer, nullable=True)  # Păstrăm Integer pentru ore/minute
    exit_time = Column(Integer, nullable=True)   # Păstrăm Integer pentru ore/minute



    
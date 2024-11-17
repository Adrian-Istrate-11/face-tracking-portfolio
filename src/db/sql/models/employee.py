from sqlalchemy import Column, Integer, String  # Corect
from src.db.sql.models import SQL_Base  # Asigură-te că SQL_Base este importat corect

class Employee(SQL_Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    start_hour = Column(Integer, nullable=False, default=21)
    end_hour = Column(Integer, nullable=False, default=4)







    

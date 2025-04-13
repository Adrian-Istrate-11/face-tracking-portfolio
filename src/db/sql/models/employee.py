from sqlalchemy import Column, Integer, String
from db.sql.connection import SQL_Base

class Employee(SQL_Base):
    __tablename__ = 'employee'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    start_hour = Column(Integer, nullable=False, default=21)
    end_hour = Column(Integer, nullable=False, default=4)

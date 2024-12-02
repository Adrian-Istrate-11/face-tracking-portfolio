from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db.sql.models import SQL_Base
from .person import Person
from .employee import Employee

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db.sql.models import SQL_Base

class Visitors(SQL_Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=True)
    name = Column(String(255), nullable=False)  
    reason = Column(String(255), nullable=False)  # Am adăugat 255 de caractere pentru "reason"
    duration_hours = Column(Integer, nullable=False)  # Păstrăm Integer pentru durata
    alert_triggered = Column(Boolean, default=False)

    # Relații
    #visitors = relationship("Person", back_populates="visits")
    #visiting_employee = relationship("Employee", back_populates="visited_by")



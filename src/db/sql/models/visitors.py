from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.sql.connection import SQL_Base
from db.sql.models.person import Person
from db.sql.models.employee import Employee

class Visitors(SQL_Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=True)
    name = Column(String(255), nullable=False)
    reason = Column(String(255), nullable=False)
    duration_hours = Column(Integer, nullable=False)
    alert_triggered = Column(Boolean, default=False)

    # Relații (dacă vrei să le activezi mai târziu)
    # person = relationship("Person", back_populates="visits")
    # employee = relationship("Employee", back_populates="visited_by")

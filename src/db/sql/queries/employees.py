from src.db.sql.connection import SQLSesssion
from src.db.sql.models import Employee
from typing import List

def add_employee_into_the_db(name: str, position: str, start_hour: int, end_hour: int) -> None:
    """
    Add an employee into the database
    """
    with SQLSesssion() as session:
        employee = Employee(
            name=name,
            position=position,
            start_hour=start_hour,
            end_hour=end_hour
        )
        session.add(employee)
        session.commit()


########## Structura pentru examen ##########

"""
def add_employee_into_the_db(name: str, position: str, start_hour: int, end_hour: int) -> Employee:
    with SQLSesssion() as session:
        employee = Employee(name=name, position=position, start_hour=start_hour, end_hour=end_hour)
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee

def get_all_employees_from_db() -> List[Employee]:
    with SQLSesssion() as session:
        return session.query(Employee).all()

def get_employee_by_id_from_db(employee_id: int) -> Employee:
    with SQLSesssion() as session:
        return session.query(Employee).filter(Employee.id == employee_id).first()

def update_employee_in_db(employee_id: int, name: str, position: str, start_hour: int, end_hour: int) -> Employee:
    with SQLSesssion() as session:
        employee = session.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            employee.name = name
            employee.position = position
            employee.start_hour = start_hour
            employee.end_hour = end_hour
            session.commit()
            session.refresh(employee)
        return employee

def delete_employee_from_db(employee_id: int) -> bool:
    with SQLSesssion() as session:
        employee = session.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            session.delete(employee)
            session.commit()
            return True
        return False
"""
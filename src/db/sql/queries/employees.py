from src.db.sql.connection import SQLSesssion
from src.db.sql.models import Employee

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
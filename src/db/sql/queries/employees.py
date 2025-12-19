from db.sql.connection import SQLSesssion
from db.sql.models.employee import Employee
from common.data_transfer_objects.employees import AddEmployeeDto, EmployeeDto

def add_employee_into_the_db(name: str, position: str, start_hour: int, end_hour: int):
    with SQLSesssion() as session:
        employee = Employee(
            name=name,
            position=position,
            start_hour=start_hour,
            end_hour=end_hour
        )
        session.add(employee)
        session.commit()

def get_all_employees_from_db() -> list[EmployeeDto]:
    with SQLSesssion() as session:
        employees = session.query(Employee).all()
        return [EmployeeDto.from_orm(emp) for emp in employees]

def delete_employee_by_id(employee_id: int) -> bool:
    with SQLSesssion() as session:
        employee = session.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            return False
        session.delete(employee)
        session.commit()
        return True

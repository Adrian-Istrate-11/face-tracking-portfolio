from fastapi import APIRouter, Response, HTTPException
from typing import List

from common.data_transfer_objects.employees import AddEmployeeDto, EmployeeDto
from db.sql.queries.employees import (
    add_employee_into_the_db,
    get_all_employees_from_db,
    delete_employee_by_id
)

router = APIRouter()

@router.put("")
def add_employee(dto: AddEmployeeDto) -> Response:
    add_employee_into_the_db(
        name=dto.name,
        position=dto.position,
        start_hour=dto.start_hour,
        end_hour=dto.end_hour,
    )
    return Response(status_code=200)

@router.get("", response_model=List[EmployeeDto])
def get_all_employees():
    employees = get_all_employees_from_db()
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found")
    return employees

@router.delete("/{employee_id}")
def delete_employee(employee_id: int):
    success = delete_employee_by_id(employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

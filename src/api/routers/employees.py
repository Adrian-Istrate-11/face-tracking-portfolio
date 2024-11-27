from fastapi import APIRouter, Response

from src.common.data_transfer_objects.employees import AddEmployeeDto
from src.db.sql.queries.employees import add_employee_into_the_db

router = APIRouter()

# GET -> fetch data
# PUT -> add data
# POST -> functions
# DELETE -> delete add

@router.put("")
def add_employee(dto: AddEmployeeDto) -> Response:
    """
    Adds an employee to the database
    """

    add_employee_into_the_db(
        name=dto.name,
        position=dto.position,
        start_hour=dto.start_hour,
        end_hour=dto.end_hour,
    )
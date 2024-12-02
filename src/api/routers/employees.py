from fastapi import APIRouter, Response
#from fastapi.exceptions import HTTPException
#from typing import List
#from src.common.data_transfer_objects.employees import EmployeeDto

from src.common.data_transfer_objects.employees import AddEmployeeDto
from src.db.sql.queries.employees import ( 
    add_employee_into_the_db,
    # get_all_employees_from_db,
    # get_employee_by_id_from_db,
    # update_employee_in_db,
    # delete_employee_from_db
)

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

######### Structura ajutatoare pentru examen #########

"""
# GET -> fetch data
@router.get("/", response_model=List[EmployeeDto])
def get_all_employees() -> List[EmployeeDto]:
    
   # Retrieves all employees from the database
    
    employees = get_all_employees_from_db()
    return employees

@router.get("/{employee_id}", response_model=EmployeeDto)
def get_employee_by_id(employee_id: int) -> EmployeeDto:
    
    #Retrieves an employee by ID from the database
    
    employee = get_employee_by_id_from_db(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# PUT -> add data
@router.put("/", response_model=EmployeeDto)
def add_employee(dto: AddEmployeeDto) -> EmployeeDto:
    
    #Adds an employee to the database
    
    employee = add_employee_into_the_db(
        name=dto.name,
        position=dto.position,
        start_hour=dto.start_hour,
        end_hour=dto.end_hour,
    )
    if employee is None:
        raise HTTPException(status_code=500, detail="Failed to add employee")
    return employee

# POST -> update data
@router.post("/{employee_id}", response_model=EmployeeDto)
def update_employee(employee_id: int, dto: AddEmployeeDto) -> EmployeeDto:
    
    #Updates an existing employee in the database
    
    employee = update_employee_in_db(
        employee_id=employee_id,
        name=dto.name,
        position=dto.position,
        start_hour=dto.start_hour,
        end_hour=dto.end_hour,
    )
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# DELETE -> delete data
@router.delete("/{employee_id}", response_class=Response)
def delete_employee(employee_id: int) -> Response:
    
    #Deletes an employee from the database
    
    success = delete_employee_from_db(employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return Response(status_code=204)
"""
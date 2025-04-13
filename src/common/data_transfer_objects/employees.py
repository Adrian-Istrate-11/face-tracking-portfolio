from pydantic import BaseModel

class AddEmployeeDto(BaseModel):
    name: str
    position: str
    start_hour: int
    end_hour: int

    class Config:
        from_attributes = True 

class EmployeeDto(AddEmployeeDto):
    id: int

    class Config:
        from_attributes = True

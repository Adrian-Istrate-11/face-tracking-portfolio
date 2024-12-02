from pydantic import BaseModel

class AddEmployeeDto(BaseModel):
    name: str
    position: str
    start_hour: int 
    end_hour: int


######### 
"""
class EmployeeDto(AddEmployeeDto):
    id: int

    class Config:
        orm_mode = True
         
 """
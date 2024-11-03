from  pydantic import BaseModel
from src.models.person import Person

class Employee(BaseModel):
    employee: Person 
    schedule: str
    work_hours = (8, 20)



    

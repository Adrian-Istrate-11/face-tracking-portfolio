from pydantic import BaseModel
from src.models.person import Person

class Maintenance(BaseModel):
    maintenance: Person
    work_hours = (21,4)
    


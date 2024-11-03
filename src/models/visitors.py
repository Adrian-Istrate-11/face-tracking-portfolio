from pydantic import BaseModel
from src.models.person import Person
from src.models.employee import Employee

class Visitors(BaseModel):
    visitors: Person
    visiting_employee: Employee
    reason: str
    duration_hours: int
    alert_triggered: bool = False

from pydantic import BaseModel

class AddVisitorDto(BaseModel):
    name: str
    reason : str
    duration_hours: int
    alert_triggered: bool
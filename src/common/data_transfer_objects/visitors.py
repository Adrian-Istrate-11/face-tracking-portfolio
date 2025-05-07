from pydantic import BaseModel

class AddVisitorDto(BaseModel):
    name: str
    reason: str
    duration_hours: int
    alert_triggered: bool

    class Config:
        from_attributes = True  

class VisitorDto(AddVisitorDto):
    id: int

    class Config:
        from_attributes = True  

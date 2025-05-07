from pydantic import BaseModel

class AddMaintenanceDto(BaseModel):
    name: str
    start_hour: int
    end_hour: int

    class Config:
        from_attributes = True  

class MaintenanceDto(AddMaintenanceDto):
    id: int

    class Config:
        from_attributes = True  

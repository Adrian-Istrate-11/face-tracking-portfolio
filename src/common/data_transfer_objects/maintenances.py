from pydantic import BaseModel

class AddMaintenanceDto(BaseModel):
    name: str
    start_hour: int
    end_hour: int
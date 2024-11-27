from fastapi import APIRouter, Response

from src.common.data_transfer_objects.maintenances import AddMaintenanceDto
from src.db.sql.queries.maintenances import add_maintenance_into_the_db

router = APIRouter()

# GET -> fetch data
# PUT -> add data
# POST -> functions
# DELETE -> delete add

@router.put("")
def add_maintenance(dto: AddMaintenanceDto) -> Response:
    """
    Adds a maintenance to the database
    """

    add_maintenance_into_the_db(
        name=dto.name,
        start_hour=dto.start_hour,
        end_hour=dto.end_hour,
       
    )
    
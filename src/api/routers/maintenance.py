from fastapi import APIRouter, Response

from common.data_transfer_objects.maintenances import AddMaintenanceDto, MaintenanceDto
from db.sql.queries.maintenances import (
    add_maintenance_into_the_db,
    get_all_maintenances_from_db,
    delete_maintenance_by_id
)

router = APIRouter()

@router.put("")
def add_maintenance(dto: AddMaintenanceDto) -> Response:
    add_maintenance_into_the_db(
        name=dto.name,
        start_hour=dto.start_hour,
        end_hour=dto.end_hour,
    )
    return Response(status_code=204)

@router.get("", response_model=list[MaintenanceDto])
def get_all_maintenances() -> list[MaintenanceDto]:
    return get_all_maintenances_from_db()

@router.delete("/{maintenance_id}")
def delete_maintenance(maintenance_id: int) -> dict:
    delete_maintenance_by_id(maintenance_id)
    return {"message": "Maintenance deleted successfully"}

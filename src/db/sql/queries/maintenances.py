from db.sql.connection import SQLSesssion
from db.sql.models import Maintenance
from common.data_transfer_objects.maintenances import MaintenanceDto


def add_maintenance_into_the_db(name: str, start_hour: int, end_hour: int) -> None:
    """
    Add a maintenance into the database
    """
    with SQLSesssion() as session:
        maintenance = Maintenance(
            name=name,
            start_hour=start_hour,
            end_hour=end_hour
        )
        session.add(maintenance)
        session.commit()

def get_all_maintenances_from_db() -> list[MaintenanceDto]:
    """
    Get all maintenances from the database
    """
    with SQLSesssion() as session:
        maintenances = session.query(Maintenance).all()
        return [MaintenanceDto.from_orm(m) for m in maintenances]

def delete_maintenance_by_id(maintenance_id: int) -> None:
    """
    Delete a maintenance by ID
    """
    with SQLSesssion() as session:
        maintenance = session.query(Maintenance).get(maintenance_id)
        if maintenance:
            session.delete(maintenance)
            session.commit()

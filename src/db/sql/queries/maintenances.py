from src.db.sql.connection import SQLSesssion
from src.db.sql.models import Maintenance




def add_maintenance_into_the_db(name: str, start_hour: int ,end_hour: int) -> None:
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
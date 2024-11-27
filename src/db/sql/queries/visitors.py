from src.db.sql.connection import SQLSesssion
from src.db.sql.models import Visitors




def add_visitor_into_the_db(name: str, reason : str ,duration_hours: int ,alert_triggered: bool=False) -> None:
    """
    Add a visitor into the database
    """
    with SQLSesssion() as session:
        visitor = Visitors(
            name=name,
            reason=reason,
            duration_hours=duration_hours,
            alert_triggered=alert_triggered
        )
        session.add(visitor)
        session.commit()
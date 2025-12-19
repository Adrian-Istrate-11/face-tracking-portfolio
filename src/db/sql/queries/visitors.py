from db.sql.connection import SQLSesssion
from db.sql.models import Visitors
from common.data_transfer_objects.visitors import VisitorDto

def add_visitor_into_the_db(name: str, reason: str, duration_hours: int, alert_triggered: bool) -> None:
    with SQLSesssion() as session:
        visitor = Visitors(
            name=name,
            reason=reason,
            duration_hours=duration_hours,
            alert_triggered=alert_triggered
        )
        session.add(visitor)
        session.commit()

def get_all_visitors_from_db() -> list[VisitorDto]:
    with SQLSesssion() as session:
        visitors = session.query(Visitors).all()
        return [VisitorDto.from_orm(visitor) for visitor in visitors]

def delete_visitor_by_id(visitor_id: int) -> None:
    with SQLSesssion() as session:
        visitor = session.query(Visitors).get(visitor_id)
        if visitor:
            session.delete(visitor)
            session.commit()

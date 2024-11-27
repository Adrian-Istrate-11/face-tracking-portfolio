from fastapi import APIRouter, Response

from src.common.data_transfer_objects.visitors import AddVisitorDto
from src.db.sql.queries.visitors import add_visitor_into_the_db

router = APIRouter()

# GET -> fetch data
# PUT -> add data
# POST -> functions
# DELETE -> delete add

@router.put("")
def add_visitor(dto: AddVisitorDto) -> Response:
    """
    Adds a visitor to the database
    """

    add_visitor_into_the_db(
        name=dto.name,
        reason=dto.reason,
        duration_hours=dto.duration_hours,
        alert_triggered=dto.alert_triggered,
    )
    
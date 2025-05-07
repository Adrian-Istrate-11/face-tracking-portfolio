from fastapi import APIRouter, Response
from src.common.data_transfer_objects.visitors import AddVisitorDto, VisitorDto
from src.db.sql.queries.visitors import (
    add_visitor_into_the_db,
    get_all_visitors_from_db,
    delete_visitor_by_id
)

router = APIRouter()

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
    return Response(status_code=204)

@router.get("", response_model=list[VisitorDto])
def get_all_visitors() -> list[VisitorDto]:
    """
    Returns all visitors from the database
    """
    return get_all_visitors_from_db()

@router.delete("/{visitor_id}")
def delete_visitor(visitor_id: int) -> dict:
    """
    Deletes a visitor by ID
    """
    delete_visitor_by_id(visitor_id)
    return {"message": "Visitor deleted successfully"}

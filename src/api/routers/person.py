from fastapi import APIRouter, Response

from src.common.data_transfer_objects.persons import AddPersonDto
from src.db.sql.queries.persons import add_person_into_the_db

router = APIRouter()

# GET -> fetch data
# PUT -> add data
# POST -> functions
# DELETE -> delete add

@router.put("")
def add_person(dto: AddPersonDto) -> Response:
    """
    Adds a person to the database
    """

    add_person_into_the_db(
        person_name=dto.person_name,
        person_type=dto.person_type,
        entry_time=dto.entry_time,
        exit_time=dto.exit_time,
    )
    
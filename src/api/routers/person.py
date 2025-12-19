from fastapi import APIRouter, Response

from common.data_transfer_objects.persons import AddPersonDto, PersonDto
from db.sql.queries.persons import (
    add_person_into_the_db,
    get_all_persons_from_db,
    delete_person_by_id
)

router = APIRouter()

@router.put("")
def add_person(dto: AddPersonDto) -> Response:
    add_person_into_the_db(
        person_name=dto.person_name,
        person_type=dto.person_type,
        entry_time=dto.entry_time,
        exit_time=dto.exit_time,
    )
    return Response(status_code=204)

@router.get("", response_model=list[PersonDto])
def get_all_persons() -> list[PersonDto]:
    return get_all_persons_from_db()

@router.delete("/{person_id}")
def delete_person(person_id: int) -> dict:
    delete_person_by_id(person_id)
    return {"message": "Person deleted successfully"}

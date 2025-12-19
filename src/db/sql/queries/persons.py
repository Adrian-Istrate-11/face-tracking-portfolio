from db.sql.connection import SQLSesssion
from db.sql.models import Person
from common.data_transfer_objects.persons import PersonDto

def add_person_into_the_db(person_name: str, person_type: str, entry_time: int, exit_time: int) -> None:
    """
    Add a person into the database
    """
    with SQLSesssion() as session:
        person = Person(
            person_name=person_name,
            person_type=person_type,
            entry_time=entry_time,
            exit_time=exit_time
        )
        session.add(person)
        session.commit()

def get_all_persons_from_db() -> list[PersonDto]:
    """
    Get all persons from the database
    """
    with SQLSesssion() as session:
        persons = session.query(Person).all()
        return [PersonDto.from_orm(person) for person in persons]

def delete_person_by_id(person_id: int) -> None:
    """
    Delete a person by ID
    """
    with SQLSesssion() as session:
        person = session.query(Person).get(person_id)
        if person:
            session.delete(person)
            session.commit()

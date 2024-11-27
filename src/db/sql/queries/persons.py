from src.db.sql.connection import SQLSesssion
from src.db.sql.models import Person




def add_person_into_the_db(name: str, person_type: str ,entry_time: int ,exit_time: int) -> None:
    """
    Add a person into the database
    """
    with SQLSesssion() as session:
        person = Person(
            name=name,
            person_type=person_type,
            entry_time=entry_time,
            exit_time=exit_time
        )
        session.add(person)
        session.commit()
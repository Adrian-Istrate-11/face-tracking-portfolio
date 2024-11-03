from pydantic import BaseModel

class Person(BaseModel):
    person_name : str
    person_type: str
    entry_time: int | None
    exit_time: int |None

    
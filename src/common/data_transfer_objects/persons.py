from pydantic import BaseModel

class AddPersonDto(BaseModel):
    person_name: str
    person_type: str
    entry_time: int
    exit_time: int
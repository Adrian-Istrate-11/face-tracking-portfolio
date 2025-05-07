from pydantic import BaseModel

class AddPersonDto(BaseModel):
    person_name: str
    person_type: str
    entry_time: int
    exit_time: int

    class Config:
        from_attributes = True  

class PersonDto(AddPersonDto):
    id: int

    class Config:
        from_attributes = True  

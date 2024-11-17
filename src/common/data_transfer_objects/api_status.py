from pydantic import BaseModel

#The class defines the structure of the data it represents.

class APIStatusDto(BaseModel):
    running: bool #Specifies that the running attribute must be of type bool (True/False).
    db_name: str  #Specifies that the db_name attribute must be of type str (string).


# running: Indicates if the API or service is operational.
# db_name: Specifies the name of the database the service is connected to.
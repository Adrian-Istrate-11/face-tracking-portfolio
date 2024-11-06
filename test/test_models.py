from src.models.person import Person
#from src.models.visitors import Visitors
#from src.models.employee import Employee
from pytest import raises


def test_person_with_valid_data()->None:
    pers=Person(
        person_name= "Alex",
        person_type="employee",
        entry_time=15,
        exit_time=16
)
    
def test_visitors_with_invalid_data()->None:
    with raises(ValueError):
        pers=Person(
        person_name= "Alex",
        person_type="employee",
        entry_time= 15,
        exit_time="ghk"
)

        
 
        
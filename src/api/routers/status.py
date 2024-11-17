from fastapi import APIRouter

from src.config import DBNAME
from src.common.data_transfer_objects.api_status import APIStatusDto


router = APIRouter()

@router.get("/status")  #Defines a GET HTTP route at the endpoint /status.
#When a client sends a GET request to this endpoint, the get_api_status function will be executed.

def get_api_status() -> APIStatusDto:
    """
    Return API status along with database that is used within the API
    """
    return APIStatusDto(
        running=True,
        db_name=DBNAME
    )
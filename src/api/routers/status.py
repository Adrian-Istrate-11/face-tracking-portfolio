from fastapi import APIRouter

from config import DBNAME
from common.data_transfer_objects.api_status import APIStatusDto


router = APIRouter()


@router.get("/status")
def get_api_status() -> APIStatusDto:
    return APIStatusDto(
        running=True,
        db_name=DBNAME
    )

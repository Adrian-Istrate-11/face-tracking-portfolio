from fastapi import APIRouter
from config import DBNAME

router = APIRouter()

@router.get("/status")
def get_status():
    return {
        "running": True,
        "db_name": DBNAME
    }

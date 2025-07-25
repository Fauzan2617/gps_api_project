from fastapi import APIRouter
from . import state

router = APIRouter()

@router.get("/gps", tags=["GPS"])
def get_latest_gps():
    if not state.latest_gps_data:
        return {"message": "Belum ada data GPS"}
    return state.latest_gps_data

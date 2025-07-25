from fastapi import APIRouter
from app.state import get_gps_state

router = APIRouter()


@router.get("/gps", tags=["GPS"])
def get_latest_gps():
    gps = get_gps_state()
    if not gps.get("time"):
        return {"message": "Belum ada data GPS"}
    return gps

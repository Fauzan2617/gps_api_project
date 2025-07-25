from app.state import gps_state
import random
import datetime

def get_latest_gps():
    # Update data simulasi
    gps_state["latitude"] += random.uniform(-0.0001, 0.0001)
    gps_state["longitude"] += random.uniform(-0.0001, 0.0001)
    gps_state["altitude"] += random.uniform(-0.01, 0.01)
    gps_state["speed"] = random.uniform(0, 1.5)
    gps_state["heading"] = random.uniform(0, 360)
    gps_state["time"] = datetime.datetime.utcnow().isoformat() + "Z"
    
    return gps_state

from threading import Lock

_gps_state = {
    "time": "",
    "latitude": 0.0,
    "longitude": 0.0,
    "altitude": 0.0,
    "speed": 0.0,
    "heading": 0.0
}
_lock = Lock()


def get_gps_state() -> dict:
    with _lock:
        return _gps_state.copy()


def update_gps_state(new_data: dict):
    with _lock:
        _gps_state.update(new_data)

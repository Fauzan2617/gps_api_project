import serial
import pynmea2
import datetime
from app.state import gps_state

def get_latest_gps():
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
        line = ser.readline().decode('utf-8', errors='ignore')
        if line.startswith('$GPRMC'):
            msg = pynmea2.parse(line)
            gps_state['latitude'] = msg.latitude
            gps_state['longitude'] = msg.longitude
            gps_state['speed'] = float(msg.spd_over_grnd) * 1.852  # knot to km/h
            gps_state['heading'] = float(msg.true_course or 0.0)
            gps_state['altitude'] = 0.0  # GPRMC tidak punya data ini
            gps_state['time'] = datetime.datetime.utcnow().isoformat() + 'Z'

    return gps_state

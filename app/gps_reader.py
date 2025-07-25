import random
import time
import datetime

def read_gps():
    now = datetime.datetime.utcnow().isoformat() + "Z"
    lat = random.uniform(-90.0, 90.0)
    lon = random.uniform(-180.0, 180.0)
    altitude = random.uniform(0.0, 10000.0)   # meters
    speed = random.uniform(0.0, 200.0)        # km/h
    heading = random.uniform(0.0, 360.0)      # degrees
    return {
        "time": now,
        "latitude": lat,
        "longitude": lon,
        "altitude": altitude,
        "speed": speed,
        "heading": heading,
    }

def main():
    print("Starting random GPS data generator (Ctrl+C to stop)...")
    try:
        while True:
            data = read_gps()
            print(data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()

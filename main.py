from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
import datetime
import threading
import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")

_current = {}

def _update_random_gps():
    global _current
    while True:
        now = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        _current = {
            "time":     now,
            "latitude": round(random.uniform(-90,   90),   6),
            "longitude":round(random.uniform(-180, 180),   6),
            "altitude": round(random.uniform(0,     5000), 2),
            "speed":    round(random.uniform(0,     120),  2),
            "heading":  round(random.uniform(0,     360),  1),
        }
        time.sleep(1)

@app.on_event("startup")
def startup():
    threading.Thread(target=_update_random_gps, daemon=True).start()

@app.get("/gps")
def get_gps():
    return _current

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

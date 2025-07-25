from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.gps_reader import get_latest_gps

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Middleware agar bisa diakses dari HP atau web eksternal
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Boleh diatur jadi domain tertentu agar lebih aman
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint JSON data GPS real-time
@app.get("/gps")
async def get_gps():
    try:
        data = get_latest_gps()
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Endpoint HTML dengan peta Leaflet
@app.get("/realtime", response_class=HTMLResponse)
async def realtime_page(request: Request):
    return templates.TemplateResponse("realtime.html", {"request": request})

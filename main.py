from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.gps_reader import get_latest_gps

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Middleware untuk akses dari HP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Boleh diubah nanti kalau mau lebih aman
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/gps")
async def get_gps():
    return get_latest_gps()

@app.get("/realtime", response_class=HTMLResponse)
async def realtime_page(request: Request):
    return templates.TemplateResponse("realtime.html", {"request": request})

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.status import router as status_router
from api.routers.employees import router as employees_router
from api.routers.person import router as person_router
from api.routers.maintenance import router as maintenance_router
from api.routers.visitors import router as visitors_router

from db.sql.init_db import init_db


app = FastAPI(
    title="Nenos Academy Face-tracking API",
    description="API for Nenos Academy Face-tracking Application",
    version="1.0.0",
)

# CORS – permite UI-ului Dash să apeleze API-ul
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # poți restrânge ulterior la domeniul UI
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inițializare DB la pornirea aplicației
@app.on_event("startup")
def on_startup():
    init_db()

# Rute API
app.include_router(status_router, prefix="/api", tags=["API"])
app.include_router(employees_router, prefix="/employees", tags=["Employees"])
app.include_router(person_router, prefix="/person", tags=["Persons"])
app.include_router(maintenance_router, prefix="/maintenance", tags=["Maintenances"])
app.include_router(visitors_router, prefix="/visitor", tags=["Visitors"])

# Root – ca să nu mai vezi 404 pe /
@app.get("/")
def root():
    return {"message": "API is running. Go to /docs"}

# Health check – pentru Render / monitorizare
@app.get("/health")
def health():
    return {"status": "ok"}

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
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(status_router, prefix="/api")
app.include_router(employees_router, prefix="/employees")
app.include_router(person_router, prefix="/person")
app.include_router(maintenance_router, prefix="/maintenance")
app.include_router(visitors_router, prefix="/visitor")

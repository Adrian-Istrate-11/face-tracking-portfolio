import uvicorn
from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from config import API_HOST, API_PORT
from api.routers.status import router as status_router
from api.routers.employees import router as employees_router
from api.routers.person import router as person_router
from api.routers.maintenance import router as maintenance_router
from api.routers.visitors import router as visitors_router

from db.sql.init_db import init_db  # <- denumirea corectă a funcției

# Create FastAPI app
app = FastAPI(
    title="Nenos Academy Face-tracking API",
    description="An API used in the for the Nenos Academy Face-tracking App",
    version="1.0.0",
)

# Include routers
app.include_router(status_router, prefix="/api", tags=["API"])
app.include_router(employees_router, prefix="/employees", tags=["Employees"])
app.include_router(person_router, prefix="/person", tags=["Persons"])
app.include_router(maintenance_router, prefix="/maintenance", tags=["Maintenances"])
app.include_router(visitors_router, prefix="/visitor", tags=["Visitors"])

# Run the app via uvicorn
if __name__ == "__main__":
    print("Initializing SQL Database")
    init_db()
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)

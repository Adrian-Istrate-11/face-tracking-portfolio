import uvicorn # is an ASGI server used to run FastAPI applications.
from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
#print(sys.path)


from src.config import API_HOST, API_PORT
from src.api.routers.status import router as status_router
from src.api.routers.employees import router as employees_router
from src.api.routers.person import router as person_router
from src.api.routers.maintenance import router as maintenance_router
from src.api.routers.visitors import router as visitors_router


from src.db.sql.init_db import init_sql_db

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
    print ("Initializing SQL Database")
    init_sql_db()
    uvicorn.run("api.main:app", host=API_HOST, port=API_PORT, reload=True)
  


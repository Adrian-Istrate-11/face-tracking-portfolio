import uvicorn # is an ASGI server used to run FastAPI applications.
from fastapi import FastAPI

from src.config import API_HOST, API_PORT
from src.api.routers.status import router as status_router


# Create FastAPI app
app = FastAPI(
    title="Nenos Academy Face-tracking API",
    description="An API used in the for the Nenos Academy Face-tracking App",
    version="1.0.0",
)

# Include routers
app.include_router(status_router, prefix="/api", tags=["API"])

# Run the app via uvicorn
if __name__ == "__main__":
    uvicorn.run("src.api.main:app", host=API_HOST, port=API_PORT, reload=True)

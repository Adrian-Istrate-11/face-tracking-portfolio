import os

DBNAME = "face_tracking"

# API (backend)
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8080"))
API_URL = f"http://{API_HOST}:{API_PORT}"

# DASH (frontend)
DASH_HOST = os.getenv("DASH_HOST", "0.0.0.0")
DASH_PORT = int(os.getenv("PORT", "8050"))

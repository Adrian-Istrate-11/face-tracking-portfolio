# src/config.py
import os

DBNAME = "face_tracking"

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8080"))
API_URL = os.getenv("API_URL", f"http://{API_HOST}:{API_PORT}")

# Render-friendly Dash config
DASH_HOST = os.getenv("DASH_HOST", "0.0.0.0")
DASH_PORT = int(os.getenv("PORT", os.getenv("DASH_PORT", "8050")))

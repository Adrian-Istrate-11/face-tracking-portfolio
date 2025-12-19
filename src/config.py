import os

DBNAME = "face_tracking"

# ───────── API ─────────
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8080"))
API_URL = f"http://{API_HOST}:{API_PORT}"

# ───────── DASH (Render-safe) ─────────
DASH_HOST = "0.0.0.0"
DASH_PORT = int(os.getenv("PORT", "8050"))

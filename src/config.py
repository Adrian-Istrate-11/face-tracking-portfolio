# src/config.py
import os

DBNAME = os.getenv("DBNAME", "face_tracking")

# API_URL trebuie să vină din Render (env var) când rulează web-ul (Dash)
# Exemplu: https://face-tracking-portfolio-1.onrender.com
API_URL = os.getenv("API_URL", "http://127.0.0.1:8080")

# Pentru local (Dash)
DASH_HOST = os.getenv("DASH_HOST", "127.0.0.1")
DASH_PORT = int(os.getenv("DASH_PORT", "8050"))

import os 


DBNAME = "face_tracking"

#API_HOST = "localhost"
API_HOST = os.getenv("API_HOST","0.0.0.0")
API_PORT = 8080
API_URL = f"http://{API_HOST}:{API_PORT}"

DASH_HOST="0.0.0.0"
DASH_PORT=8050
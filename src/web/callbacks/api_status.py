# src/web/callbacks/api_status.py
import requests
from dash import Input, Output

from src.config import API_URL

def register_api_status_callbacks(app):
    @app.callback(
        Output("api-status-text", "children"),
        Input("webapp-refresh-timer", "n_intervals"),
        prevent_initial_call=False,
    )
    def _check_api(_):
        try:
            r = requests.get(f"{API_URL}/health", timeout=5)
            if r.status_code == 200:
                return "API:  online"
            return f"API:  status {r.status_code}"
        except Exception:
            return "API:  offline"

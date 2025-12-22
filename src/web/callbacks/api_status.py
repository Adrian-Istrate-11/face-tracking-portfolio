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
            r = requests.get(f"{API_URL}/", timeout=5)
            return f"API: online  ({r.status_code}) @ {API_URL}"
        except Exception as e:
            return f"API: offline  @ {API_URL} | {type(e).__name__}: {e}"

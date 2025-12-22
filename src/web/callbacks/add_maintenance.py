import requests
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from common.data_transfer_objects.maintenances import AddMaintenanceDto


def register_add_maintenance_callbacks(app: Dash) -> None:

    @app.callback(
        Output("add-maintenance-feedback", "children"),
        Output("add-maintenance-feedback", "style"),
        Output("add-maintenance-feedback-interval", "disabled"),
        Output("add-maintenance-name", "value"),
        Output("add-maintenance-start_hour", "value"),
        Output("add-maintenance-end_hour", "value"),
        Input("add-maintenance-button", "n_clicks"),
        State("add-maintenance-name", "value"),
        State("add-maintenance-start_hour", "value"),
        State("add-maintenance-end_hour", "value"),
        prevent_initial_call=True,
    )
    def add_maintenance(n, name, start, end):
        if not n:
            raise PreventUpdate

        dto = AddMaintenanceDto(name=name, start_hour=start, end_hour=end)

        resp = requests.put(f"{API_URL}/maintenance", json=dto.dict(), timeout=5)
        if resp.status_code in (200, 204):
            return "Added.", {"color": "green"}, False, "", "", ""

        return "Failed.", {"color": "red"}, True, name, start, end

import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.maintenances import AddMaintenanceDto



def register_add_maintenance_callbacks(app: Dash) -> None:
    """
    Register add maintenance callbacks
    """
    @app.callback(
        Output('maintenance-content', "children"),
        [
            Input("add-maintenance-button", "n_clicks"),
            Input("add-maintenance-name", "value"),
            Input("add-maintenance-start_hour", "value"),
            Input("add-maintenance-end_hour", "value"),
        ]
    )
    def send_maintenance_info_to_api(_: int,maintenance_name: str, maintenance_start_hour: int, maintenance_end_hour: int):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-maintenance-button":
            dto = AddMaintenanceDto(
                name=maintenance_name,
                start_hour=maintenance_start_hour,
                end_hour=maintenance_end_hour,
            
            )
            response = requests.put(f"{API_URL}/maintenance", timeout=5, data=dto.json())
            return response.status_code

        raise PreventUpdate
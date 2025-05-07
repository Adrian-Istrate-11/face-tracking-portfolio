import requests
from dash import Dash, html, callback_context
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
    def send_maintenance_info_to_api(n_clicks, maintenance_name, maintenance_start_hour, maintenance_end_hour):
        if n_clicks is None:
            raise PreventUpdate

        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-maintenance-button":
            dto = AddMaintenanceDto(
                name=maintenance_name,
                start_hour=maintenance_start_hour,
                end_hour=maintenance_end_hour
            )
            response = requests.put(f"{API_URL}/maintenance", timeout=5, data=dto.json())

            if response.status_code in (200, 204):
                return html.Div([
                    html.P("Maintenance added successfully!", style={"color": "green"})
                ])

            return html.Div([
                html.P(f"Error adding maintenance: {response.status_code}", style={"color": "red"})
            ])

        raise PreventUpdate

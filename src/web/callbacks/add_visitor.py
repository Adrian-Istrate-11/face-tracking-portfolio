import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.visitors import AddVisitorDto



def register_add_visitor_callbacks(app: Dash) -> None:
    """
    Register add visitor callbacks
    """
    @app.callback(
        Output('webapp-visitor-content', "children"),
        [
            Input("add-visitor-button", "n_clicks"),
            Input("add-visitor-name", "value"),
            Input("add-visitor-reason", "value"),
            Input("add-visitor-duration_hours", "value"),
            Input("add-visitor-alert_triggered", "checked"),
        ]
    )
    def send_visitor_info_to_api(_: int, visitor_name: str, visitor_reason: str, visitor_duration_hours: int, visitor_alert_triggered: bool):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-animal-button":
            dto = AddVisitorDto(
                name=visitor_name,
                reason=visitor_reason,
                duration_hours=visitor_duration_hours,
                alert_triggered=visitor_alert_triggered,
            )
            response = requests.put(f"{API_URL}/visitors", timeout=5, data=dto.json())
            return response.status_code

        raise PreventUpdate
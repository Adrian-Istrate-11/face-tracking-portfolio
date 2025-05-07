import requests
from dash import Dash, html, callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.visitors import AddVisitorDto

def register_add_visitor_callbacks(app: Dash) -> None:
    """
    Register add visitor callbacks
    """
    @app.callback(
        Output('visitor-content', "children"),
        [
            Input("add-visitor-button", "n_clicks"),
            Input("add-visitor-name", "value"),
            Input("add-visitor-reason", "value"),
            Input("add-visitor-duration_hours", "value"),
            Input("add-visitor-alert_triggered", "checked"),
        ]
    )
    def send_visitor_info_to_api(n_clicks, visitor_name, visitor_reason, visitor_duration_hours, visitor_alert_triggered):
        if n_clicks is None:
            raise PreventUpdate

        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-visitor-button":
            dto = AddVisitorDto(
                name=visitor_name,
                reason=visitor_reason,
                duration_hours=visitor_duration_hours,
                alert_triggered=visitor_alert_triggered if visitor_alert_triggered is not None else False
            )
            response = requests.put(f"{API_URL}/visitor", timeout=5, data=dto.json())

            if response.status_code in (200, 204):
                return html.Div([
                    html.P("Visitor added successfully!", style={"color": "green"})
                ])

            return html.Div([
                html.P(f"Error adding visitor: {response.status_code}", style={"color": "red"})
            ])

        raise PreventUpdate

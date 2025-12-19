import requests
from dash import Dash, html, no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from config import API_URL
from common.data_transfer_objects.visitors import AddVisitorDto


def register_add_visitor_callbacks(app: Dash) -> None:

    @app.callback(
        Output("add-visitor-feedback", "children"),
        Output("add-visitor-feedback", "style"),
        Output("add-visitor-feedback-interval", "disabled"),
        Output("add-visitor-name", "value"),
        Output("add-visitor-reason", "value"),
        Output("add-visitor-duration_hours", "value"),
        Output("add-visitor-alert_triggered", "checked"),
        Input("add-visitor-button", "n_clicks"),
        State("add-visitor-name", "value"),
        State("add-visitor-reason", "value"),
        State("add-visitor-duration_hours", "value"),
        State("add-visitor-alert_triggered", "checked"),
        prevent_initial_call=True,
    )
    def add_visitor(n, name, reason, duration, alert):
        if not n:
            raise PreventUpdate

        dto = AddVisitorDto(
            name=name,
            reason=reason,
            duration_hours=duration,
            alert_triggered=bool(alert),
        )

        resp = requests.put(f"{API_URL}/visitor", json=dto.dict(), timeout=5)

        if resp.status_code in (200, 204):
            return "Added.", {"color": "green"}, False, "", "", None, False

        return "Failed.", {"color": "red"}, True, name, reason, duration, alert

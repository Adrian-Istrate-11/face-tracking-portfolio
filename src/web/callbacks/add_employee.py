import requests
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from src.common.data_transfer_objects.employees import AddEmployeeDto


def register_add_employee_callbacks(app: Dash) -> None:

    @app.callback(
        Output("add-employee-feedback", "children"),
        Output("add-employee-feedback", "style"),
        Output("add-employee-feedback-interval", "disabled"),
        Output("add-employee-name", "value"),
        Output("add-employee-position", "value"),
        Output("add-employee-start_hour", "value"),
        Output("add-employee-end_hour", "value"),
        Input("add-employee-button", "n_clicks"),
        State("add-employee-name", "value"),
        State("add-employee-position", "value"),
        State("add-employee-start_hour", "value"),
        State("add-employee-end_hour", "value"),
        prevent_initial_call=True,
    )
    def add_employee(n_clicks, name, position, start_hour, end_hour):
        if not n_clicks:
            raise PreventUpdate

        # Validare
        if not all([name, position, start_hour, end_hour]):
            return (
                " Complete all fields.",
                {"display": "block", "color": "orange"},
                True,
                name,
                position,
                start_hour,
                end_hour,
            )

        dto = AddEmployeeDto(name=name, position=position, start_hour=start_hour, end_hour=end_hour)

        url = f"{API_URL}/employees"
        try:
            resp = requests.put(url, json=dto.dict(), timeout=10)
        except Exception as exc:
            return (
                f" Request failed to {url}\n{type(exc).__name__}: {exc}",
                {"display": "block", "color": "red", "whiteSpace": "pre-wrap"},
                True,
                name,
                position,
                start_hour,
                end_hour,
            )

        # Afișează clar răspunsul API, indiferent de status
        if resp.status_code in (200, 201, 204):
            return (
                f" Added via {url} (status {resp.status_code})",
                {"display": "block", "color": "green"},
                False,
                "",
                "",
                "",
                "",
            )

        return (
            f" API error via {url} (status {resp.status_code})\n{resp.text}",
            {"display": "block", "color": "red", "whiteSpace": "pre-wrap"},
            True,
            name,
            position,
            start_hour,
            end_hour,
        )

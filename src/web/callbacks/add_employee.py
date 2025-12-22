import requests
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from common.data_transfer_objects.employees import AddEmployeeDto


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

        if not all([name, position, start_hour, end_hour]):
            return (
                "Complete all fields.",
                {"display": "block", "color": "orange"},
                True,
                name,
                position,
                start_hour,
                end_hour,
            )

        dto = AddEmployeeDto(
            name=name,
            position=position,
            start_hour=start_hour,
            end_hour=end_hour,
        )

        try:
            resp = requests.put(f"{API_URL}/employees", json=dto.dict(), timeout=5)
        except Exception as exc:
            return (
                f"Error: {exc}",
                {"display": "block", "color": "red"},
                True,
                name,
                position,
                start_hour,
                end_hour,
            )

        if resp.status_code in (200, 204):
            return "Employee added.", {"display": "block", "color": "green"}, False, "", "", "", ""

        return "Failed.", {"display": "block", "color": "red"}, True, name, position, start_hour, end_hour

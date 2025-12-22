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

        if not all([name, position, start_hour, end_hour]):
            return (
                "All fields are required.",
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
            resp = requests.put(
                f"{API_URL}/employees",
                json=dto.dict(),
                timeout=10,
            )
        except Exception as e:
            return (
                f"Request error: {e}",
                {"display": "block", "color": "red"},
                True,
                name,
                position,
                start_hour,
                end_hour,
            )

        if resp.status_code in (200, 201, 204):
            return (
                "Employee added successfully.",
                {"display": "block", "color": "green"},
                False,
                "",
                "",
                "",
                "",
            )

        return (
            f"API error {resp.status_code}: {resp.text}",
            {"display": "block", "color": "red"},
            True,
            name,
            position,
            start_hour,
            end_hour,
        )


def register_get_employees_callback(app: Dash) -> None:
    @app.callback(
        Output("get-employees-output", "children"),
        Input("get-employees-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def get_all_employees(n_clicks):
        if not n_clicks:
            raise PreventUpdate

        try:
            resp = requests.get(f"{API_URL}/employees", timeout=10)
            resp.raise_for_status()
            employees = resp.json()
        except Exception as e:
            return f"Error fetching employees: {e}"

        if not employees:
            return "No employees found."

        return [
            f"ID {e['id']} | {e['name']} | {e['position']} | {e['start_hour']} - {e['end_hour']}"
            for e in employees
        ]

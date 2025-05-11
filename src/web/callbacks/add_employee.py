import requests
import dash
from dash import Dash, html, no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from src.common.data_transfer_objects.employees import AddEmployeeDto


def register_add_employee_callbacks(app: Dash) -> None:
    """Register callbacks for Add / Show / Delete Employee."""

    # 1) ADD employee → feedback + auto-dismiss + clear inputs
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
    def add_employee(
        n_clicks,
        name, position, start_hour, end_hour,
    ):
        if not n_clicks:
            raise PreventUpdate

        if not all([name, position, start_hour, end_hour]):
            return (
                "Please complete all fields.",
                {"display": "block", "color": "orange"},
                True,
                name, position, start_hour, end_hour,
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
                timeout=5,
                json=dto.dict()
            )
        except Exception as exc:
            return (
                f"Error adding employee: {exc}",
                {"display": "block", "color": "red"},
                True,
                name, position, start_hour, end_hour,
            )

        if resp.status_code in (200, 204):
            return (
                "Employee added successfully.",
                {"display": "block", "color": "green"},
                False,      # enable auto-dismiss
                "", "", "", "",  # clear inputs
            )

        return (
            f"Failed to add employee ({resp.status_code}).",
            {"display": "block", "color": "red"},
            True,
            name, position, start_hour, end_hour,
        )

    # 2) Auto-dismiss feedback after interval fires
    @app.callback(
        Output("add-employee-feedback", "style", allow_duplicate=True),
        Output("add-employee-feedback-interval", "disabled", allow_duplicate=True),
        Input("add-employee-feedback-interval", "n_intervals"),
        prevent_initial_call=True,
    )
    def hide_add_employee_feedback(_):
        return {"display": "none"}, True

    # 3) SHOW ALL employees
    @app.callback(
        Output("get-employees-output", "children"),
        Input("get-employees-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def get_all_employees(n_clicks):
        if not n_clicks:
            raise PreventUpdate

        try:
            resp = requests.get(f"{API_URL}/employees", timeout=5)
            if resp.status_code == 200:
                employees = resp.json()
                return html.Ul(
                    [
                        html.Li(
                            f"{e['id']}: {e['name']} "
                            f"({e['position']}, {e['start_hour']}-{e['end_hour']})"
                        )
                        for e in employees
                    ]
                )
            return html.P("Failed to fetch employees.", style={"color": "orange"})
        except Exception as exc:
            return html.P(f"Error fetching employees: {exc}", style={"color": "red"})

    # 4) DELETE employee → feedback + clear delete-ID + clear list
    @app.callback(
        Output("delete-employee-output", "children"),
        Output("delete-employee-id", "value"),
        Output("get-employees-output", "children", allow_duplicate=True),
        Input("delete-employee-button", "n_clicks"),
        State("delete-employee-id", "value"),
        prevent_initial_call=True,
    )
    def delete_employee(n_clicks, employee_id):
        if not n_clicks or employee_id is None:
            raise PreventUpdate

        try:
            resp = requests.delete(f"{API_URL}/employees/{employee_id}", timeout=5)
        except Exception as exc:
            return html.P(f"Error deleting employee: {exc}", style={"color": "red"}), no_update, no_update

        if resp.status_code == 200:
            return html.P("Employee deleted successfully.", style={"color": "green"}), "", ""
        return html.P("Could not delete employee.", style={"color": "orange"}), no_update, no_update

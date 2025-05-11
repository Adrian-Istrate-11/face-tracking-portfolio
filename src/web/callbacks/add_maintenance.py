import requests
import dash
from dash import Dash, html, no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from src.common.data_transfer_objects.maintenances import AddMaintenanceDto


def register_add_maintenance_callbacks(app: Dash) -> None:
    """Register callbacks for Add / Show / Delete Maintenance."""

    # 1) ADD maintenance → feedback + auto‐dismiss + clear inputs + clear list
    @app.callback(
        Output("add-maintenance-feedback", "children"),
        Output("add-maintenance-feedback", "style"),
        Output("add-maintenance-feedback-interval", "disabled"),
        Output("add-maintenance-name", "value"),
        Output("add-maintenance-start_hour", "value"),
        Output("add-maintenance-end_hour", "value"),
        Output("get-maintenances-output", "children", allow_duplicate=True),
        Input("add-maintenance-button", "n_clicks"),
        State("add-maintenance-name", "value"),
        State("add-maintenance-start_hour", "value"),
        State("add-maintenance-end_hour", "value"),
        prevent_initial_call=True,
    )
    def add_maintenance(n_clicks, name, start_hour, end_hour):
        if not n_clicks:
            raise PreventUpdate

        if not all([name, start_hour, end_hour]):
            return (
                "Please complete all fields.",
                {"display": "block", "color": "orange"},
                True,
                name, start_hour, end_hour,
                no_update,
            )

        dto = AddMaintenanceDto(name=name, start_hour=start_hour, end_hour=end_hour)

        try:
            resp = requests.put(
                f"{API_URL}/maintenance",
                json=dto.dict(),
                timeout=5,
            )
        except Exception as exc:
            return (
                f"Error adding maintenance: {exc}",
                {"display": "block", "color": "red"},
                True,
                name, start_hour, end_hour,
                no_update,
            )

        if resp.status_code in (200, 204):
            return (
                "Maintenance added successfully.",
                {"display": "block", "color": "green"},
                False,
                "", "", "",
                "",  # clear list
            )

        return (
            f"Failed to add maintenance ({resp.status_code}).",
            {"display": "block", "color": "red"},
            True,
            name, start_hour, end_hour,
            no_update,
        )

    # 2) Auto‐dismiss feedback
    @app.callback(
        Output("add-maintenance-feedback", "style", allow_duplicate=True),
        Output("add-maintenance-feedback-interval", "disabled", allow_duplicate=True),
        Input("add-maintenance-feedback-interval", "n_intervals"),
        prevent_initial_call=True,
    )
    def hide_add_maintenance_feedback(_):
        return {"display": "none"}, True

    # 3) SHOW ALL maintenances → populate list on button click
    @app.callback(
        Output("get-maintenances-output", "children"),
        Input("get-maintenances-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def get_all_maintenances(n_clicks):
        if not n_clicks:
            raise PreventUpdate

        try:
            resp = requests.get(f"{API_URL}/maintenance", timeout=5)
            if resp.status_code == 200:
                items = resp.json()
                return html.Ul([
                    html.Li(f"{m['id']}: {m['name']} ({m['start_hour']}-{m['end_hour']})")
                    for m in items
                ])
            return html.P("Failed to fetch maintenances.", style={"color": "orange"})
        except Exception as exc:
            return html.P(f"Error fetching maintenances: {exc}", style={"color": "red"})

    # 4) DELETE maintenance → feedback + clear delete-ID + clear list
    @app.callback(
        Output("delete-maintenance-output", "children"),
        Output("delete-maintenance-id", "value"),
        Output("get-maintenances-output", "children", allow_duplicate=True),
        Input("delete-maintenance-button", "n_clicks"),
        State("delete-maintenance-id", "value"),
        prevent_initial_call=True,
    )
    def delete_maintenance(n_clicks, maintenance_id):
        if not n_clicks or maintenance_id is None:
            raise PreventUpdate

        try:
            resp = requests.delete(f"{API_URL}/maintenance/{maintenance_id}", timeout=5)
        except Exception as exc:
            return (
                html.P(f"Error deleting maintenance: {exc}", style={"color": "red"}),
                no_update,
                no_update,
            )

        if resp.status_code == 200:
            return (
                html.P("Maintenance deleted successfully.", style={"color": "green"}),
                "",   # clear delete-ID
                "",   # clear list
            )

        return (
            html.P("Could not delete maintenance.", style={"color": "orange"}),
            no_update,
            no_update,
        )

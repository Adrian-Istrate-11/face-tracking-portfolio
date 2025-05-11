import requests
import dash
from dash import Dash, html, no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from src.common.data_transfer_objects.persons import AddPersonDto


def register_add_person_callbacks(app: Dash) -> None:
    """Register callbacks for Add / Show / Delete Person."""

    # ADD persoană → feedback + auto-dismiss + clear inputs
    @app.callback(
        Output("add-person-feedback", "children"),
        Output("add-person-feedback", "style"),
        Output("add-person-feedback-interval", "disabled"),
        Output("add-person-name", "value"),
        Output("add-person-person_type", "value"),
        Output("add-person-entry_time", "value"),
        Output("add-person-exit_time", "value"),
        Input("add-person-button", "n_clicks"),
        State("add-person-name", "value"),
        State("add-person-person_type", "value"),
        State("add-person-entry_time", "value"),
        State("add-person-exit_time", "value"),
        prevent_initial_call=True,
    )
    def add_person(
        n_clicks,
        name, ptype, entry, exit_,
    ):
        if not n_clicks:
            raise PreventUpdate

        dto = AddPersonDto(
            person_name=name,
            person_type=ptype,
            entry_time=entry,
            exit_time=exit_,
        )
        try:
            resp = requests.put(f"{API_URL}/person", timeout=5, data=dto.json())
        except Exception as exc:
            return (
                f"Error adding person: {exc}",
                {"display": "block", "color": "red"},
                True,
                name, ptype, entry, exit_,
            )

        if resp.status_code in (200, 204):
            return (
                "Person added successfully.",
                {"display": "block", "color": "green"},
                False,
                "", "", "", "",
            )
        return (
            f"Error adding person: {resp.status_code}",
            {"display": "block", "color": "red"},
            True,
            name, ptype, entry, exit_,
        )

    # Auto-dismiss feedback
    @app.callback(
        Output("add-person-feedback", "style", allow_duplicate=True),
        Output("add-person-feedback-interval", "disabled", allow_duplicate=True),
        Input("add-person-feedback-interval", "n_intervals"),
        prevent_initial_call=True,
    )
    def hide_add_feedback(_):
        return {"display": "none"}, True

    # SHOW ALL PERSONS
    @app.callback(
        Output("get-persons-output", "children"),
        Input("get-persons-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def get_all_persons(n_clicks):
        if not n_clicks:
            raise PreventUpdate

        try:
            resp = requests.get(f"{API_URL}/person", timeout=5)
            if resp.status_code == 200:
                persons = resp.json()
                return html.Ul(
                    [html.Li(f"{p['id']}: {p['person_name']} ({p['person_type']})") for p in persons]
                )
            return html.P("Failed to fetch persons.", style={"color": "orange"})
        except Exception as exc:
            return html.P(f"Error fetching persons: {exc}", style={"color": "red"})

    # DELETE person → feedback + clear delete-ID + clear lista
    @app.callback(
        Output("delete-person-output", "children"),
        Output("delete-person-id", "value"),
        Output("get-persons-output", "children", allow_duplicate=True),
        Input("delete-person-button", "n_clicks"),
        State("delete-person-id", "value"),
        prevent_initial_call=True,
    )
    def delete_person(n_clicks, person_id):
        if not n_clicks or person_id is None:
            raise PreventUpdate

        try:
            resp = requests.delete(f"{API_URL}/person/{person_id}", timeout=5)
        except Exception as exc:
            return html.P(f"Error deleting person: {exc}", style={"color": "red"}), no_update, no_update

        if resp.status_code == 200:
            # clear both the ID input and the list
            return html.P("Person deleted successfully.", style={"color": "green"}), "", ""

        return html.P("Could not delete person.", style={"color": "orange"}), no_update, no_update

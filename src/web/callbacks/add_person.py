import requests
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from common.data_transfer_objects.persons import AddPersonDto


def register_add_person_callbacks(app: Dash) -> None:

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
    def add_person(n, name, ptype, entry, exit_):
        if not n:
            raise PreventUpdate

        dto = AddPersonDto(
            person_name=name,
            person_type=ptype,
            entry_time=entry,
            exit_time=exit_,
        )

        resp = requests.put(f"{API_URL}/person", json=dto.dict(), timeout=5)

        if resp.status_code in (200, 204):
            return "Added.", {"color": "green"}, False, "", "", "", ""

        return "Failed.", {"color": "red"}, True, name, ptype, entry, exit_

import requests
from dash import Dash, html
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.persons import AddPersonDto


def register_add_person_callbacks(app: Dash) -> None:
    """
    Register add person callbacks
    """

    #  PUT person
    @app.callback(
        Output('person-content', "children"),
        [
            Input("add-person-button", "n_clicks"),
            Input("add-person-name", "value"),
            Input("add-person-person_type", "value"),
            Input("add-person-entry_time", "value"),
            Input("add-person-exit_time", "value"),
        ]
    )
    def send_person_info_to_api(_: int, person_name: str, person_type: str, person_entry_time: int, person_exit_time: int):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-person-button":
            dto = AddPersonDto(
                person_name=person_name,
                person_type=person_type,
                entry_time=person_entry_time,
                exit_time=person_exit_time
            )
            response = requests.put(f"{API_URL}/person", timeout=5, data=dto.json())

            if response.status_code in (200, 204):
                return html.Div([
                    html.P(" Person added successfully!", style={"color": "green"})
                ])
            return html.Div([
                html.P(f" Error adding person: {response.status_code}", style={"color": "red"})
            ])
        raise PreventUpdate

    #  GET all persons
    @app.callback(
        Output("get-persons-output", "children"),
        [Input("get-persons-button", "n_clicks")]
    )
    def get_all_persons(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        try:
            response = requests.get(f"{API_URL}/person", timeout=5)
            if response.status_code == 200:
                persons = response.json()
                return html.Ul([
                    html.Li(f"{p['id']}: {p['person_name']} ({p['person_type']})") for p in persons
                ])
            else:
                return html.P(" Failed to fetch persons", style={"color": "orange"})
        except Exception as e:
            return html.P(f" Error: {e}", style={"color": "red"})

    #  DELETE person
    @app.callback(
        Output("delete-person-output", "children"),
        [Input("delete-person-button", "n_clicks"),
         Input("delete-person-id", "value")]
    )
    def delete_person_by_id_callback(n_clicks, person_id):
        if not n_clicks or not person_id:
            raise PreventUpdate
        try:
            response = requests.delete(f"{API_URL}/person/{person_id}", timeout=5)
            if response.status_code == 200:
                return html.P("🗑️ Person deleted successfully!", style={"color": "green"})
            else:
                return html.P(" Could not delete person.", style={"color": "orange"})
        except Exception as e:
            return html.P(f" Error: {e}", style={"color": "red"})

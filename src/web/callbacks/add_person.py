import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.persons import AddPersonDto


def register_add_person_callbacks(app: Dash) -> None:
    """
    Register add person callbacks
    """
    @app.callback(
        Output('webapp-person-content', "children"),
        [
            Input("add-person-button", "n_clicks"),
            Input("add-person-name", "value"),
            Input("add-person-person_type", "value"),
            Input("add-person-entry_time", "value"),
            Input("add-person-exit_time", "value"),
        ]
    )
    def send_person_info_to_api(_: int, person_name: str, person_type: str,person_entry_time: int, person_exit_time: int):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-animal-button":
            dto = AddPersonDto(
                name=person_name ,
                person_type=person_type,
                entry_time=person_entry_time,
                exit_time=person_exit_time
            )
            response = requests.put(f"{API_URL}/persons", timeout=5, data=dto.json())
            return response.status_code

        raise PreventUpdate
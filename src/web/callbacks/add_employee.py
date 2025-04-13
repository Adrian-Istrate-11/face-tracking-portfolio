import requests
from dash import Dash, html
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.employees import AddEmployeeDto


def register_add_employee_callbacks(app: Dash) -> None:
    """
    Register add employee callbacks
    """
    @app.callback(
        Output('employee-content', "children"),
        [
            Input("add-employee-button", "n_clicks"),
            Input("add-employee-name", "value"),
            Input("add-employee-position", "value"),
            Input("add-employee-start_hour", "value"),
            Input("add-employee-end_hour", "value"),
        ]
    )
    def send_employee_info_to_api(n_clicks: int, employee_name: str, employee_position: str, employee_start_hour: int, employee_end_hour: int):
        trigger = callback_context.triggered[0]

        # Execută doar dacă a fost apăsat butonul
        if trigger["prop_id"].split('.')[0] == "add-employee-button":
            if not all([employee_name, employee_position, employee_start_hour, employee_end_hour]):
                return html.Div("Please complete all fields.", style={"color": "orange"})

            dto = AddEmployeeDto(
                name=employee_name,
                position=employee_position,
                start_hour=employee_start_hour,
                end_hour=employee_end_hour,
            )

            try:
                response = requests.put(
                    f"{API_URL}/employees",
                    timeout=5,
                    json=dto.dict()  #JSON corect, nu data + .json()
                )

                if response.status_code == 200:
                    return html.Div("Employee added successfully!", style={"color": "green"})
                else:
                    return html.Div(f"Failed to add employee. Status code: {response.status_code}", style={"color": "red"})

            except requests.RequestException as e:
                return html.Div(f"Error connecting to API: {e}", style={"color": "red"})

        raise PreventUpdate

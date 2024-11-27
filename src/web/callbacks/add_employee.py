import requests
from dash import Dash

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
        Output('webapp-content', "children"),
        [
            Input("add-employee-button", "n_clicks"),
            Input("add-employee-name", "value"),
            Input("add-employee-position", "value"),
            Input("add-employee-start_hour", "value"),
            Input("add-employee-end_hour", "value"),
        ]
    )
    def send_employee_info_to_api(_: int, employee_name: str, employee_position: str, employee_start_hour: int, employee_end_hour: int):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-employee-button":
            dto = AddEmployeeDto(
                name=employee_name,
                position=employee_position,
                start_hour=employee_start_hour,
                end_hour=employee_end_hour,
            )
            response = requests.put(f"{API_URL}/employees", timeout=5, data=dto.json())
            return response.status_code

        raise PreventUpdate
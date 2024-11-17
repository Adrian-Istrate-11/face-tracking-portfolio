import requests
from dash import Dash

from dash.dependencies import Input, Output

from src.config import API_URL, DBNAME
from src.common.data_transfer_objects.api_status import APIStatusDto
from src.web.components.api_status import (
    ApiStatusOK,
    ApiStatusNOK,
    ApiStatusError
)


def register_api_status_callbacks(app: Dash) -> None:
    """
    Register api status callbacks
    """
    @app.callback(
        Output('webapp-content', "children"),
        [Input("webapp-refresh-timer", "n_intervals")]
    )
    def check_api_status(_):
        try:
            response = requests.get(f"{API_URL}/api/status", timeout=5)
            status = APIStatusDto(**response.json())
            assert status.running
            assert status.db_name == DBNAME
            if response.status_code == 200:
                return ApiStatusOK().render()

            return ApiStatusNOK(response.status_code).render()
        except requests.exceptions.RequestException as ex:
            return ApiStatusError(ex).render()
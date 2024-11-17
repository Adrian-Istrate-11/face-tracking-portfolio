import requests # Imports the requests library, which is used to send HTTP requests in Python.
from dash import Dash # is used to build web applications.

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
            response = requests.get(f"{API_URL}/api/status", timeout=5) # This sends a GET request to the /api/status endpoint of the API, which is expected to return the current status of the API
            status = APIStatusDto(**response.json()) #If the request is successful, the response is parsed as JSON, and an instance of the APIStatusDto class is created with the data.
            assert status.running
            assert status.db_name == DBNAME #this ensures that the correct database is being used.
            if response.status_code == 200: #If the API returns a status code of 200 (OK), it means the API is functioning properly.
                return ApiStatusOK().render() # If the response code is not 200, it returns the ApiStatusNOK component with the status code passed in

            return ApiStatusNOK(response.status_code).render()
        except requests.exceptions.RequestException as ex:
            return ApiStatusError(ex).render() # shows an error message,indicating that something went wrong when checking the API status.


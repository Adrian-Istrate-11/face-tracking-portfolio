import dash_mantine_components as dmc # provides a collection of UI components for Dash apps. 
# Here, it's used for creating text components.

from dash_iconify import DashIconify # Imports the DashIconify component, 
#which is used to display icons from the Iconify icon library.

from dash import html # is used to create HTML components.

from src.web.components.base import DashAppBaseComponent

# check for icons here: https://icon-sets.iconify.design/

class ApiStatusOK(DashAppBaseComponent):  # Purpose: Represents the "API is connected" state 

    def __init__(self):
        pass

    def render(self): # Creates an HTML div element
        return html.Div(children=[
            DashIconify(icon="fluent-color:checkmark-circle-48"),
            dmc.Text("API is connected"),
        ])
# This component is used when the API is working properly,
# indicating that the connection to the API is successful.

class ApiStatusNOK(DashAppBaseComponent): # Purpose: Represents the "API is yielding" state (when the API is up but is returning an unexpected or non-200 status code).

    def __init__(self, status_code: int):
        self.status_code = status_code

    def render(self):
        return html.Div(children=[
            DashIconify(icon="fluent-color:error-circle-48"),
            dmc.Text("API is yielding"),
            dmc.Text(str(self.status_code)),
        ])
# This component is used when the API is up but returns an error status code (like 500, 404, etc.).

class ApiStatusError(DashAppBaseComponent): # Purpose: Represents the "API is down" state (when the API is not reachable or there was an exception while trying to communicate with it).

    def __init__(self, exception: Exception):
        self.exception = exception

    def render(self):
        return html.Div(children=[
            DashIconify(icon="fluent-color:dismiss-circle-48"),
            dmc.Text("API is down"),
            dmc.Text(str(self.exception)),
        ])
#This component is used when the API is completely unreachable or has thrown an exception.
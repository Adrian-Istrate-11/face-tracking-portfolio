from dash import Dash

from .api_status import register_api_status_callbacks


def register_all_callbacks(app: Dash) -> None:
    """
    Register all component callbacks
    """
    register_api_status_callbacks(app)

# register all component callbacks for the app.
# A callback is a function in Dash that listens for user interaction with UI components and then updates other components.
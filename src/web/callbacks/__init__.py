from dash import Dash

from .api_status import register_api_status_callbacks


def register_all_callbacks(app: Dash) -> None:
    """
    Register all component callbacks
    """
    register_api_status_callbacks(app)
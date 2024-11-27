from dash import Dash

from .api_status import register_api_status_callbacks
from .add_employee import register_add_employee_callbacks
from .add_person import register_add_person_callbacks
from .add_maintenance import register_add_maintenance_callbacks
from .add_visitor import  register_add_visitor_callbacks

def register_all_callbacks(app: Dash) -> None:
    """
    Register all component callbacks
    """
    #register_api_status_callbacks(app)
    register_add_employee_callbacks(app)
    register_add_person_callbacks(app)
    register_add_maintenance_callbacks(app)
    register_add_visitor_callbacks(app)


# register all component callbacks for the app.
# A callback is a function in Dash that listens for user interaction with UI components and then updates other components.
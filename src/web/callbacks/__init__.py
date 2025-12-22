from dash import Dash

from src.web.callbacks.add_employee import (
    register_add_employee_callbacks,
    register_get_employees_callback,
)
from src.web.callbacks.add_person import register_add_person_callbacks
from src.web.callbacks.add_visitor import register_add_visitor_callbacks
from src.web.callbacks.add_maintenance import register_add_maintenance_callbacks
from src.web.callbacks.api_status import register_api_status_callbacks


def register_all_callbacks(app: Dash) -> None:
    register_api_status_callbacks(app)
    register_add_employee_callbacks(app)
    register_get_employees_callback(app)
    register_add_person_callbacks(app)
    register_add_visitor_callbacks(app)
    register_add_maintenance_callbacks(app)

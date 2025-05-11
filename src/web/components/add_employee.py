import dash_mantine_components as dmc
from dash import html, dcc

from src.web.components.base import DashAppBaseComponent


class AddEmployeeComponent(DashAppBaseComponent):
    def __init__(self):
        super().__init__()

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(id="add-employee-name", label="Employee Name:", w=200),
                dmc.TextInput(id="add-employee-position", label="Position:", w=200),
                dmc.TextInput(id="add-employee-start_hour", label="Start Hour:", w=200),
                dmc.TextInput(id="add-employee-end_hour", label="End Hour:", w=200),

                dmc.Group(
                    children=[
                        dmc.Button(id="add-employee-button", children="Add Employee", w=200),
                        dmc.Button(id="get-employees-button", children="Show All Employees", color="blue", w=200),
                    ]
                ),

                # Feedback area (hidden until needed)
                html.Div(id="add-employee-feedback", style={"display": "none"}),

                # Auto-dismiss interval for feedback
                dcc.Interval(
                    id="add-employee-feedback-interval",
                    interval=3_000,    # 3 seconds
                    n_intervals=0,
                    disabled=True,
                ),

                # Container for listing employees
                html.Div(id="get-employees-output"),

                dmc.Divider(),

                dmc.NumberInput(id="delete-employee-id", label="Employee ID to Delete", w=200),
                dmc.Button(id="delete-employee-button", children="Delete Employee", color="red", w=200),
                html.Div(id="delete-employee-output"),
            ]
        )

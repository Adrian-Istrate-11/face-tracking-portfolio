import dash_mantine_components as dmc
from dash import html, dcc

from src.web.components.base import DashAppBaseComponent


class AddMaintenanceComponent(DashAppBaseComponent):
    def __init__(self):
        super().__init__()

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(id="add-maintenance-name", label="Maintenance Name:", w=200),
                dmc.TextInput(id="add-maintenance-start_hour", label="Start Hour:", w=200),
                dmc.TextInput(id="add-maintenance-end_hour", label="End Hour:", w=200),

                dmc.Group(
                    children=[
                        dmc.Button(id="add-maintenance-button", children="Add Maintenance", w=200),
                        dmc.Button(id="get-maintenances-button", children="Show All Maintenances", color="blue", w=200),
                    ]
                ),

                html.Div(id="add-maintenance-feedback", style={"display": "none"}),

                dcc.Interval(
                    id="add-maintenance-feedback-interval",
                    interval=3000,
                    n_intervals=0,
                    disabled=True,
                ),

                html.Div(id="get-maintenances-output"),

                dmc.Divider(),

                dmc.NumberInput(id="delete-maintenance-id", label="Maintenance ID to Delete", w=200),
                dmc.Button(id="delete-maintenance-button", children="Delete Maintenance", color="red", w=200),
                html.Div(id="delete-maintenance-output"),
            ]
        )

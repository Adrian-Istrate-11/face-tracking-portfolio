import dash_mantine_components as dmc
from dash import html, dcc

from src.web.components.base import DashAppBaseComponent


class AddVisitorComponent(DashAppBaseComponent):
    def __init__(self):
        super().__init__()

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(id="add-visitor-name", label="Visitor Name:", w=200),
                dmc.TextInput(id="add-visitor-reason", label="Reason for Visit:", w=200),
                dmc.NumberInput(id="add-visitor-duration_hours", label="Duration Hours:", w=200),
                dmc.Checkbox(
                    id="add-visitor-alert_triggered",
                    label="Was the alarm turned on?",
                    value=False,
                    mb=10,
                ),
                dmc.Group(
                    children=[
                        dmc.Button(id="add-visitor-button", children="Add Visitor", w=200),
                        dmc.Button(id="get-visitors-button", children="Show All Visitors", color="blue", w=200),
                    ]
                ),
                html.Div(id="add-visitor-feedback", style={"display": "none"}),
                dcc.Interval(
                    id="add-visitor-feedback-interval",
                    interval=3000,
                    n_intervals=0,
                    disabled=True,
                ),
                html.Div(id="get-visitors-output"),
                dmc.Divider(),
                dmc.NumberInput(id="delete-visitor-id", label="Visitor ID to Delete", w=200),
                dmc.Button(id="delete-visitor-button", children="Delete Visitor", color="red", w=200),
                html.Div(id="delete-visitor-output"),
            ]
        )

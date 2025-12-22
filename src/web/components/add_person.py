import dash_mantine_components as dmc
from dash import html, dcc

from src.web.components.base import DashAppBaseComponent


class AddPersonComponent(DashAppBaseComponent):
    def __init__(self):
        super().__init__()

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(id="add-person-name", label="Person Name:", w=200),
                dmc.TextInput(id="add-person-person_type", label="Person Type:", w=200),
                dmc.TextInput(id="add-person-entry_time", label="Entry Time:", w=200),
                dmc.TextInput(id="add-person-exit_time", label="Exit Time:", w=200),

                dmc.Group(
                    children=[
                        dmc.Button(id="add-person-button", children="Add Person", w=200),
                        dmc.Button(id="get-persons-button", children="Show All Persons", color="blue", w=200),
                    ]
                ),

                html.Div(id="add-person-feedback", style={"display": "none"}),

                dcc.Interval(
                    id="add-person-feedback-interval",
                    interval=3_000,
                    n_intervals=0,
                    disabled=True,
                ),

                html.Div(id="get-persons-output"),

                dmc.Divider(),

                dmc.NumberInput(id="delete-person-id", label="Person ID to Delete", w=200),
                dmc.Button(id="delete-person-button", children="Delete Person", color="red", w=200),
                html.Div(id="delete-person-output"),
            ]
        )

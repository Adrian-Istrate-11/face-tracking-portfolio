import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class AddVisitorComponent(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="add-visitor-name",
                    label="Visitor Name:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-visitor-reason",
                    label="Visitor Reason:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-visitor-duration_hours",
                    label="Duration hours:",
                    w=200
                ),
                dmc.Checkbox(
                    id="add-visitor-alert_triggered",
                    label="Was the alarm turned on?",
                    mb=10
                ),
                dmc.Button(
                    id="add-visitor-button",
                    children="Add visitor",
                    w=200,
                ),
            ],
        )
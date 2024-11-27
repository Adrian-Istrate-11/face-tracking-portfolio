import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class AddMaintenanceComponent(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="add-maintenance-name",
                    label="Maintenance Name:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-maintenance-start_hour",
                    label="Maintenance Start-hour:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-maintenance-end_hour",
                    label="Maintenance End-hour:",
                    w=200
                ),
                dmc.Button(
                    id="add-maintenance-button",
                    children="Add maintenance",
                    w=200,
                ),
            ],
        )
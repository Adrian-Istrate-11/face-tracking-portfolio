import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class AddPersonComponent(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="add-person-name",
                    label="Person Name:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-person-person_type",
                    label="Person Type:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-person-entry_time",
                    label="Person Entry-time",
                    w=200
                ),
                dmc.TextInput(
                    id="add-person-exit_time",
                    label="Person Exit-time1",
                    w=200
                ),
                dmc.Button(
                    id="add-person-button",
                    children="Add person",
                    w=200,
                ),
            ],
        )
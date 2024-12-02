import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class AddEmployeeComponent(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
                children=[
                # dmc.AccordionItem(


                # )
                dmc.TextInput(
                    id="add-employee-name",
                    label="Employee Name:",
                    w=200
                ),
                
                dmc.TextInput(
                    id="add-employee-position",
                    label="Employee Position:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-employee-start_hour",
                    label="Start_hour:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-employee-end_hour",
                    label="End_hour",
                    w=200
                ),
                dmc.Button(
                    id="add-employee-button",
                    children="Add employee",
                    w=200,
                ),
            ],
        )
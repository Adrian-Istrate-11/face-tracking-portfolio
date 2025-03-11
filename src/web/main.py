import dash
import dash_mantine_components as dmc
from dash import html, dcc
import sys
import os
from dash_iconify import DashIconify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
#print(sys.path)
from config import DASH_HOST, DASH_PORT
from src.web.callbacks import register_all_callbacks
from src.web.components.header import Header
from src.web.components.add_employee import AddEmployeeComponent
from src.web.components.add_person import AddPersonComponent
from src.web.components.add_maintenance import AddMaintenanceComponent
from src.web.components.add_visitor import AddVisitorComponent
from src.web.components.header import Subtitle
from src.web.callbacks.api_status import register_api_status_callbacks

# Create the Dash app
app = dash.Dash(__name__)
app.title = "API Status Checker"

# App layout
app.layout = dmc.MantineProvider(
    children=dmc.Stack(

        children=[
            # Header
            html.Div(
                id='webapp-header',
                children=[
                    Header("Face-Tracking App").render(),  # Render the header
                    dmc.Divider(variant="solid"),
                    Subtitle("Track employees, maintenances, visitors, and persons activities").render(),  # Render the subtitle
                ],
            ),
            dmc.Divider(variant="solid"),
            # Accordion menu
            dmc.Accordion(
                children=[
                    dmc.AccordionItem(
                        value="employee",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text(
                                    "Employee",
                                    style={
                                        "fontFamily":"Arial, sans-serif",
                                        "fontSize": "24px", 
                                        "fontWeight": "bold",
                                        "color": "black",

                                    },
                                ),
                                icon=DashIconify(
                                    icon="tabler:user",
                                    color="green", 
                                    width=20,   
                                ),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id='employee-content', children=AddEmployeeComponent().render())
                            )
                        ],
                    ),
                    dmc.AccordionItem(
                        value="person",
                        children=[dmc.AccordionControl(
                                dmc.Text(
                                    "Person",
                                    style={
                                        "fontFamily":"Arial, sans-serif",
                                        "fontSize": "24px", 
                                        "fontWeight": "bold",
                                        "color": "black",

                                    },
                                ),
                                icon=DashIconify(
                                    icon="tabler:user",
                                    color="green", 
                                    width=20,   
                                ),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id='person-content', children=AddPersonComponent().render())
                            )
                        ],
                    ),
                    dmc.AccordionItem(
                        value="visitor",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text(
                                    "Visitor",
                                    style={
                                        "fontFamily":"Arial, sans-serif",
                                        "fontSize": "24px", 
                                        "fontWeight": "bold",
                                        "color": "black",

                                    },
                                ),
                            icon=DashIconify(
                                    icon="tabler:user",
                                    color="green", 
                                    width=20,   
                                ),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id='visitor-content', children=AddVisitorComponent().render())
                            )
                        ],
                    ),
                    dmc.AccordionItem(
                        value="maintenance",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text(
                                    "Maintenance",
                                    style={
                                        "fontFamily":"Arial, sans-serif",
                                        "fontSize": "24px", 
                                        "fontWeight": "bold",
                                        "color": "black",

                                    },
                                ),
                            icon=DashIconify(
                                    icon="tabler:user",
                                    color="green", 
                                    width=20,   
                                ),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id='maintenance-content', children=AddMaintenanceComponent().render())
                            )
                        ],
                    ),
                ]
            ),
            # Page refresh
            dcc.Interval(
                id="webapp-refresh-timer",
                interval=1 * 60 * 1000,  # 1 minute in milliseconds
                n_intervals=0,  # Number of times the interval has fired
            ),
        ]
    )
)

# Register all component callbacks
register_all_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run(host=DASH_HOST, port=str(DASH_PORT),debug=True)
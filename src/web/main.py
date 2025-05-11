import os
import sys

import dash
import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify

# Adaugă root-ul proiectului în PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.config import DASH_HOST, DASH_PORT
from src.web.callbacks import register_all_callbacks
from src.web.components.header import Header, Subtitle
from src.web.components.add_employee import AddEmployeeComponent
from src.web.components.add_person import AddPersonComponent
from src.web.components.add_visitor import AddVisitorComponent
from src.web.components.add_maintenance import AddMaintenanceComponent
from src.web.callbacks.api_status import register_api_status_callbacks

# ─────────────── Create the Dash app ───────────────
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,  # permite callback-uri către componente dinamic generate
)
app.title = "Face-Tracking App"

# ─────────────── App layout ───────────────
app.layout = dmc.MantineProvider(
    children=dmc.Stack(
        children=[

            # Header
            html.Div(
                id="webapp-header",
                children=[
                    Header("Face-Tracking App").render(),
                    dmc.Divider(variant="solid"),
                    Subtitle("Track employees, maintenances, visitors, and persons activities").render(),
                ],
            ),
            dmc.Divider(variant="solid"),

            # Accordion
            dmc.Accordion(
                children=[
                    dmc.AccordionItem(
                        value="employee",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text("Employee", style={
                                    "fontFamily": "Arial, sans-serif",
                                    "fontSize": "24px", "fontWeight": "bold"
                                }),
                                icon=DashIconify(icon="tabler:user", color="green", width=20),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id="employee-content", children=AddEmployeeComponent().render())
                            ),
                        ],
                    ),
                    dmc.AccordionItem(
                        value="person",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text("Person", style={
                                    "fontFamily": "Arial, sans-serif",
                                    "fontSize": "24px", "fontWeight": "bold"
                                }),
                                icon=DashIconify(icon="tabler:user", color="green", width=20),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id="person-content", children=AddPersonComponent().render())
                            ),
                        ],
                    ),
                    dmc.AccordionItem(
                        value="visitor",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text("Visitor", style={
                                    "fontFamily": "Arial, sans-serif",
                                    "fontSize": "24px", "fontWeight": "bold"
                                }),
                                icon=DashIconify(icon="tabler:user", color="green", width=20),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id="visitor-content", children=AddVisitorComponent().render())
                            ),
                        ],
                    ),
                    dmc.AccordionItem(
                        value="maintenance",
                        children=[
                            dmc.AccordionControl(
                                dmc.Text("Maintenance", style={
                                    "fontFamily": "Arial, sans-serif",
                                    "fontSize": "24px", "fontWeight": "bold"
                                }),
                                icon=DashIconify(icon="tabler:user", color="green", width=20),
                            ),
                            dmc.AccordionPanel(
                                html.Div(id="maintenance-content", children=AddMaintenanceComponent().render())
                            ),
                        ],
                    ),
                ]
            ),

            # Page‐refresh timer (opțional)
            dcc.Interval(id="webapp-refresh-timer", interval=60_000, n_intervals=0),

            # ───────── Hero Image & Footer ─────────
            html.Div(style={"marginTop": "3rem"}),
            dmc.Center(
                # imaginea trebuie să fie în src/web/assets/FaceTrackingApp.jpg
                dmc.Image(src="/assets/FaceTrackingApp.jpg", opacity=0.75, maw=400),
            ),
            html.Div(style={"height": "1rem"}),
            dmc.Text(
                "© 2025 Face-Tracking App. All rights reserved.",
                ta="center", c="dimmed", size="md"
            ),
        ]
    )
)

# ───────── Register callbacks ───────── 
register_all_callbacks(app)
register_api_status_callbacks(app)

# ───────── Run server ─────────
if __name__ == "__main__":
    app.run(host=DASH_HOST, port=str(DASH_PORT), debug=True)
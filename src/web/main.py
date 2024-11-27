import dash
import dash_mantine_components as dmc
from dash import html, dcc

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
#print(sys.path)
from src.web.callbacks import register_all_callbacks
from src.web.components.header import Header
#from src.web.components.loading import Loading
from src.web.components.add_employee import AddEmployeeComponent
from src.web.components.add_person import AddPersonComponent
from src.web.components.add_maintenance import AddMaintenanceComponent
from src.web.components.add_visitor import AddVisitorComponent

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
                children=Header("Face-Tracking App").render()
            ),
            dmc.Divider(variant="solid"),
            # Main content
            html.Div(
                id='webapp-content',
                children=[
                    #Loading().render()
                    AddEmployeeComponent().render(),   
                ]
            ),
             html.Div(
                id='webapp-maintenance-content',
                children=[
                    AddMaintenanceComponent().render(), 
                ]
            
            ),
            html.Div(
                id='webapp-visitor-content',
                children=[
                    AddVisitorComponent().render(), 
                ]
            ),
            html.Div(
                id='webapp-person-content',
                children=[
                    AddPersonComponent().render(), 
                ]
            ),
            # Page refresh
            dcc.Interval(
                id="webapp-refresh-timer",
                interval=1 * 60 * 1000,  # 1 minutes in milliseconds
                n_intervals=0,  # Number of times the interval has fired
            ),
        ]
    )
)

# Register all component callbacks
register_all_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
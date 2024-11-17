import dash
import dash_mantine_components as dmc
from dash import html, dcc

from src.web.callbacks import register_all_callbacks
from src.web.components.header import Header
from src.web.components.loading import Loading

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
                children=Header("Shelter App").render()
            ),
            dmc.Divider(variant="solid"),
            # Main content
            html.Div(
                id='webapp-content',
                children=[
                    Loading().render()
                ]
            ),
            # Page refresh
            dcc.Interval(
                id="webapp-refresh-timer",
                interval=1 * 60 * 1000,  # 5 minutes in milliseconds
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
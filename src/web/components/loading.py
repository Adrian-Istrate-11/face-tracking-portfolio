import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent

# The Loading class is a custom Dash component that renders a loading spinner.
# It centers the spinner in the middle of the screen using dmc.Center.
# The spinner is created using the dmc.Loader component, which is configured to be
# blue, extra-large, and use the "dots" variant for the animation.

class Loading(DashAppBaseComponent):

    def __init__(self) -> None:
        pass

    def render(self) -> dmc.Paper:
        return dmc.Center(
            children=[
                dmc.Loader(color="blue", size="xl", variant="dots")
            ]
        )
# render Method: defines how the Loading component will be rendered as a UI element in the Dash app.

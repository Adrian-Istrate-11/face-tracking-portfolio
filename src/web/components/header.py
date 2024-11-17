import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent

# The Header class defines a custom UI component for a header section in the Dash app.
class Header(DashAppBaseComponent):

    def __init__(self, title: str) -> None:
        self.title=title

    def render(self) -> dmc.Paper:
        return dmc.Paper(
            children=dmc.Title(self.title, order=1, style={"margin": "0", "color": "white"}),
            shadow="xs",
            style={
                "backgroundColor": "#4C6EF5",
                "padding": "10px"
            },
        )
# render Method: returns a Dash component that represents the rendered version of the Header. It uses dmc.
# Paper to create a wrapper around the title.
# dmc.Paper: This is a Mantine component that provides a styled container (similar to a div) with properties like shadow and padding.
# The children of dmc.Paper is a dmc.Title, which renders the title text.

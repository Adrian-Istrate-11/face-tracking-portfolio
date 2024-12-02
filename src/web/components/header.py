
# render Method: returns a Dash component that represents the rendered version of the Header. It uses dmc.
# Paper to create a wrapper around the title.
# dmc.Paper: This is a Mantine component that provides a styled container (similar to a div) with properties like shadow and padding.
# The children of dmc.Paper is a dmc.Title, which renders the title text.
import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent

class Header(DashAppBaseComponent):
    def __init__(self, title: str) -> None:
        self.title = title

    def render(self) -> dmc.Paper:
        return dmc.Paper(
            children=dmc.Title(
                self.title,
                order=1,
                style={
                    "margin": "0",
                    "box-shadow": "0 10px 20px rgba(0, 0, 0, 0.25)",
                    "color": "black",  
                    "textAlign": "center", 
                     "fontFamily": "Courier New, Courier, monospace",
                    "fontSize": "3.5rem",  
                    "letterSpacing": "1px"
                },
            ),
            shadow="xs",
            style={
                "backgroundColor": "#A8DADC",  # Light green background
                "padding": "20px",  # Increase padding for better spacing
                "borderRadius": "10px",  # Add rounded corners for style
                "width": "100%",  # Make the header span full width
                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.1)",  # Soft shadow
            },
        )
    
######################################


class Subtitle(DashAppBaseComponent):
    def __init__(self, subtitle: str) -> None:
        self.subtitle = subtitle

    def render(self) -> dmc.Paper:
        return dmc.Paper(
            children=dmc.Title(
                self.subtitle,  
                order=3,  
                style={
                    "margin": "0",
                    "color": "#555",  
                    "textAlign": "center",  
                    "fontFamily": "Georgia, serif",  
                    "fontSize": "1.2rem",  
                    "fontStyle": "italic",  
                },
            ),
            shadow="xs",
            style={
                "backgroundColor": "#F1FAEE",  
                "padding": "10px",  
                "borderRadius": "5px",
                "marginTop": "0",  
                "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.05)", 
            },
        )
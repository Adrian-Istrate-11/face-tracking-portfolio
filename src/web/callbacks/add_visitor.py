import requests
from dash import Dash, html, no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.config import API_URL
from src.common.data_transfer_objects.visitors import AddVisitorDto

def register_add_visitor_callbacks(app: Dash) -> None:
    """Register callbacks for Add / Show / Delete Visitor."""

    # ─── 1) ADD visitor → PUT /visitor ─────────────────────────────────────────
    @app.callback(
        Output("add-visitor-feedback", "children"),
        Output("add-visitor-feedback", "style"),
        Output("add-visitor-feedback-interval", "disabled"),
        Output("add-visitor-name", "value"),
        Output("add-visitor-reason", "value"),
        Output("add-visitor-duration_hours", "value"),
        Output("add-visitor-alert_triggered", "checked"),
        Input("add-visitor-button", "n_clicks"),
        State("add-visitor-name", "value"),
        State("add-visitor-reason", "value"),
        State("add-visitor-duration_hours", "value"),
        State("add-visitor-alert_triggered", "checked"),
        prevent_initial_call=True,
    )
    def add_visitor(n_clicks, name, reason, duration_hours, alert_triggered):
        if not n_clicks:
            raise PreventUpdate

        # validare
        if not name or not reason or duration_hours is None:
            return (
                "Please complete all fields.",
                {"display": "block", "color": "orange"},
                True,
                name,
                reason,
                duration_hours,
                alert_triggered,
            )

        dto = AddVisitorDto(
            name=name,
            reason=reason,
            duration_hours=duration_hours,
            alert_triggered=alert_triggered or False,
        )
        try:
            resp = requests.put(f"{API_URL}/visitor", json=dto.dict(), timeout=5)
        except Exception as exc:
            return (
                f"Error adding visitor: {exc}",
                {"display": "block", "color": "red"},
                True,
                name,
                reason,
                duration_hours,
                alert_triggered,
            )

        if resp.status_code in (200, 204):
            # succes: golim toate câmpurile
            return (
                "Visitor added successfully.",
                {"display": "block", "color": "green"},
                False,   # pornește intervalul pentru auto-dismiss
                "",      # clear name
                "",      # clear reason
                None,    # clear duration_hours
                False,   # clear checkbox
            )

        return (
            f"Failed to add visitor ({resp.status_code}).",
            {"display": "block", "color": "red"},
            True,
            name,
            reason,
            duration_hours,
            alert_triggered,
        )

    # auto-dismiss feedback ADD
    @app.callback(
        Output("add-visitor-feedback", "style", allow_duplicate=True),
        Output("add-visitor-feedback-interval", "disabled", allow_duplicate=True),
        Input("add-visitor-feedback-interval", "n_intervals"),
        prevent_initial_call=True,
    )
    def hide_add_feedback(_):
        return {"display": "none"}, True


    # ─── 2) SHOW all visitors → GET /visitor ──────────────────────────────────
    @app.callback(
        Output("get-visitors-output", "children"),
        Input("get-visitors-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def get_all_visitors(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        try:
            resp = requests.get(f"{API_URL}/visitor", timeout=5)
            if resp.status_code == 200:
                visitors = resp.json()
                return html.Ul([
                    html.Li(
                        f"{v['id']}: {v['name']} "
                        f"(Reason: {v['reason']}, Duration: {v['duration_hours']}h, "
                        f"Alarm: {'Yes' if v['alert_triggered'] else 'No'})"
                    )
                    for v in visitors
                ])
            return html.P("Failed to fetch visitors.", style={"color": "orange"})
        except Exception as exc:
            return html.P(f"Error fetching visitors: {exc}", style={"color": "red"})


    # ─── 3) DELETE visitor → DELETE /visitor/{id} ─────────────────────────────
    @app.callback(
        Output("delete-visitor-output", "children"),
        Output("delete-visitor-id", "value"),
        Output("get-visitors-output", "children", allow_duplicate=True),
        Input("delete-visitor-button", "n_clicks"),
        State("delete-visitor-id", "value"),
        prevent_initial_call=True,
    )
    def delete_visitor(n_clicks, visitor_id):
        if not n_clicks:
            raise PreventUpdate

        if visitor_id is None:
            # nu ați introdus ID
            return (
                html.P("Please enter an ID to delete.", style={"color": "orange"}),
                None,    # clear NumberInput
                no_update,
            )

        try:
            resp = requests.delete(f"{API_URL}/visitor/{visitor_id}", timeout=5)
        except Exception as exc:
            return (
                html.P(f"Error deleting visitor: {exc}", style={"color": "red"}),
                None,      # clear NumberInput
                no_update, # nu ating lista
            )

        if resp.status_code == 200:
            # succes: mesaj + reset câmp + golire listă
            return (
                html.P("Visitor deleted successfully.", style={"color": "green"}),
                None,   # clear NumberInput
                "",     # clear lista afișată
            )

        return (
            html.P(f"Could not delete visitor ({resp.status_code})", style={"color": "orange"}),
            None,
            no_update,
        )

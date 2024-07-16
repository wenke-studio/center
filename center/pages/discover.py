import reflex as rx

from center import layouts


@layouts.dashboard
def discover():
    """
    The Discover Page

    This page renders charts, tables, and other data visualizations
    to help users discover insights.
    """
    return rx.box(rx.text("Discover Page"))

import reflex as rx

from center.frontend import layouts
from center.frontend.components import charts

line_example = [
    {"name": "A", "a": 100, "b": 200, "e": 300, "f": 400},
    {"name": "B", "a": 100, "b": 200, "c": 500, "e": 250, "f": 10},
    {"name": "C", "b": 100, "f": 200},
    {"name": "D", "e": 100, "b": 200, "a": 150},
]

LINES = [
    charts.Line(data_key="a", stroke="red"),
    charts.Line(data_key="b", stroke="blue"),
    charts.Line(data_key="c", stroke="green"),
    charts.Line(data_key="d", stroke="orange"),
    charts.Line(data_key="e", stroke="var(--red-7)"),
    charts.Line(data_key="f", stroke="pink"),
]


@rx.page(route="/discover")
@layouts.dashboard
def discover():
    """
    The Discover Page

    This page renders charts, tables, and other data visualizations
    to help users discover insights.
    """
    return rx.box(
        rx.text("Discover Page"),
        rx.card(
            charts.line(
                data=line_example,
                data_key="name",
                lines=LINES,
            )
        ),
        class_name="pr-4",
    )

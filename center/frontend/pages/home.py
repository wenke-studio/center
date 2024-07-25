import reflex as rx

from center.frontend import layouts


@rx.page(route="/")
@layouts.dashboard
def home():
    """
    The home page

    the page displays a welcome message for debugging purposes.
    """

    return rx.box(
        rx.text("Welcome to the Home Page!"),
    )

import reflex as rx


def home():
    """
    The home page

    the page displays a welcome message for debugging purposes.
    """

    return rx.container(
        rx.text("Welcome to the Home Page!"),
    )

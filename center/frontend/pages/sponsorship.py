import reflex as rx

from center.frontend import layouts


@rx.page(route="/sponsorship")
@layouts.dashboard
def sponsorship():
    """
    The Sponsorship Page

    This page displays information about the sponsorship opportunities
    available to users.
    """
    return rx.box(
        rx.text("Sponsorship Page"),
    )

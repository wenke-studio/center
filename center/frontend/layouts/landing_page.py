from typing import Callable

import reflex as rx


def landing_page(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Welcome"),
                page(),
            )
        ),
        class_name="h-screen grid place-items-center",
    )

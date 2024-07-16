from typing import Callable

import reflex as rx

from .sidebar import sidebar

items = [
    {"text": "Discover", "href": "/discover"},
    {"text": "sponsorship", "href": "/sponsorship"},
]


def dashboard(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.hstack(
        sidebar(items),
        page(),
        class_name="w-full h-screen grid grid-cols-[auto,1fr]",
        # height="100vh",
        # width="100vw",
    )

import reflex as rx


def hgroup(title: str, description: str) -> rx.Component:
    return rx.box(
        rx.heading(title),
        rx.text(description),
        class_name="pb-4",
    )

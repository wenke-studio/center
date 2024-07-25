import reflex as rx


def logo(title: str) -> rx.Component:
    return rx.center(
        rx.icon("network", class_name="w-8 h-auto color-red-500"),
        rx.heading(title),
        class_name="w-full gap-2 pb-4",
    )

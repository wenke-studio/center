import reflex as rx

FULLSCREEN = "w-full h-screen"


def merge(*class_names: list[str]) -> str:
    return " ".join(class_names)


def layout(content: rx.Component, class_name: str = "") -> rx.Component:
    return rx.box(
        rx.vstack(content, footer(), class_name="gap-8"),
        class_name=merge(
            FULLSCREEN,
            "grid place-items-center p-4",
            class_name,
        ),
    )


def footer() -> rx.Component:
    return rx.hstack(
        rx.text("2024 Wenke"),
        rx.spacer(),
        rx.link("Privacy", href="#"),
        rx.link("Terms", href="#"),
        class_name="w-full",
    )

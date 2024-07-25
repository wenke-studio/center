import reflex as rx


def social_login():
    return rx.vstack(
        rx.button("Google", class_name="w-full active:scale-95", variant="outline"),
        rx.button("GitHub", class_name="w-full active:scale-95", variant="outline"),
        rx.button("Faceback", class_name="w-full active:scale-95", variant="outline"),
        class_name="gap-4 w-full",
    )

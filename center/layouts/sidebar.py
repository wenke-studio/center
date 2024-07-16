import reflex as rx

from center.pages.auth.state import AuthState

Item = dict[str, str]


def sidebar(items: list[Item]) -> rx.Component:
    return rx.grid(
        rx.link(rx.heading("Title"), href="/"),
        rx.vstack(
            *[rx.link(item["text"], href=item["href"]) for item in items],
            class_name="overflow-y-auto h-full gap-4",
        ),
        rx.vstack(
            rx.button("Logout", on_click=AuthState.logout),
            rx.text("© 2024"),
        ),
        class_name="h-screen w-fit grid-rows-[auto,1fr,auto] p-4 overflow-hidden gap-8",
        border_right="1px solid gray",
    )

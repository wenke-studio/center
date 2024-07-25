import reflex as rx

from .states import AuthState


def loading() -> rx.Component:
    return rx.center(rx.spinner(size="3"))


def login_required(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    def wrapper(*args, **kwargs):
        return rx.fragment(
            rx.cond(
                AuthState.is_authenticated,
                page(*args, **kwargs),
                loading(),
            ),
        )

    wrapper.__name__ = page.__name__
    return wrapper

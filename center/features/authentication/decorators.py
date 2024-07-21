import reflex as rx

from .states import AuthState


def loading() -> rx.Component:
    return rx.center(rx.spinner(size="3"))


def require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    def wrapper():
        return rx.Fragment(
            rx.cond(AuthState.is_authenticated, page(), loading()),
        )

    wrapper.__name__ = page.__name__
    return wrapper

import reflex as rx

from center import layouts
from center.features.authentication.states import LoginState


@rx.page(route="/auth/login")
@layouts.landing_page
def login() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("Login"),
            rx.input(
                placeholder="Email",
                on_blur=LoginState.set_email,
                id="email",
            ),
            rx.input(
                placeholder="Password",
                on_blur=LoginState.set_password,
                id="password",
            ),
            rx.link("Signup", href="/auth/signup"),
            rx.button(
                "Login",
                type="button",
                on_click=LoginState.on_submit,
            ),
            rx.cond(
                LoginState.error,
                rx.text(LoginState.error, class_name="text-red-500"),
            ),
        ),
        on_mount=LoginState.on_mount,
    )

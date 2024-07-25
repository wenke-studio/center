import reflex as rx

from center import layouts
from center.features.authentication.states import RegisterState


@rx.page(route="/auth/signup")
@layouts.landing_page
def signup() -> rx.Component:
    return rx.card(
        # rx.form(
        rx.vstack(
            rx.text("Signup"),
            rx.input(
                placeholder="Email",
                on_blur=RegisterState.set_email,
                id="email",
            ),
            rx.input(
                placeholder="Password",
                on_blur=RegisterState.set_password,
                id="password",
            ),
            rx.input(
                placeholder="Confirm Password",
                on_blur=RegisterState.set_confirm_password,
                id="confirm_password",
            ),
            rx.button(
                "Signup",
                type="button",
                on_click=RegisterState.on_submit,
            ),
            rx.hstack(
                rx.text("Already have an account?"),
                rx.link("Login", href="/auth/login"),
            ),
            rx.cond(
                RegisterState.error,
                rx.text(RegisterState.error, class_name="text-red-500"),
            ),
        ),
        on_mount=RegisterState.on_mount,
        # on_submit=RegisterState.on_submit,
        # ),
    )

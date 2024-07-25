import reflex as rx

from center.features.authentication.states import RegisterState

from . import ui


def register_card():
    return rx.card(
        rx.vstack(
            ui.logo(title="Wenke"),
            ui.hgroup(
                title="Create an account",
                description="Enter your email to create your account.",
            ),
            rx.form(
                rx.grid(
                    rx.text("Email"),
                    rx.input(
                        id="email",
                        placeholder="name@email.com",
                        class_name="w-full",
                        on_blur=RegisterState.set_email,
                    ),
                    rx.text("Password"),
                    rx.input(
                        id="password",
                        type="password",
                        placeholder="******",
                        class_name="w-full",
                        on_blur=RegisterState.set_password,
                    ),
                    rx.text("Confirm Password"),
                    rx.input(
                        id="confirm_password",
                        type="password",
                        placeholder="******",
                        class_name="w-full",
                        on_blur=RegisterState.set_confirm_password,
                    ),
                    rx.cond(
                        RegisterState.error,
                        rx.text(
                            RegisterState.error,
                            class_name="text-red-500 col-span-2 w-full",
                        ),
                    ),
                    rx.button(
                        "Register",
                        type="button",
                        class_name="w-full col-span-2",
                        on_click=RegisterState.on_submit,
                    ),
                    class_name="grid-cols-[auto,1fr] gap-4",
                ),
                on_mount=RegisterState.on_mount,
            ),
            rx.hstack(
                rx.text("Already have an account?"),
                rx.link("Login", href="/auth/login"),
            ),
            rx.divider(class_name="my-4"),
            rx.text("Or Continue With"),
            ui.social_login(),
        )
    )


@rx.page(route="/auth/signup")
def signup() -> rx.Component:
    return ui.layout(content=register_card())

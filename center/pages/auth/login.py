import reflex as rx

from center.features.authentication.states import LoginState

from . import ui


def login_card():
    return rx.card(
        rx.vstack(
            ui.logo(title="Wenke"),
            ui.hgroup(
                title="Login",
                description="Welcome back! Please sign in to continue.",
            ),
            ui.social_login(),
            rx.divider(class_name="my-4"),
            rx.form(
                rx.grid(
                    rx.text("Email"),
                    rx.input(
                        id="email",
                        placeholder="name@email.com",
                        class_name="w-full",
                        on_blur=LoginState.set_email,
                    ),
                    rx.text("Password"),
                    rx.input(
                        id="password",
                        type="password",
                        placeholder="******",
                        class_name="w-full",
                        on_blur=LoginState.set_password,
                    ),
                    rx.cond(
                        LoginState.error,
                        rx.text(
                            LoginState.error,
                            class_name="text-red-500 col-span-2",
                        ),
                        rx.text(
                            "",
                            class_name="col-span-2",
                        ),
                    ),
                    rx.button(
                        "Login with Email",
                        type="button",
                        class_name="w-full col-span-2",
                        on_click=LoginState.on_submit,
                    ),
                    class_name="grid-cols-[auto,1fr] gap-4",
                ),
                on_mount=LoginState.on_mount,
            ),
            rx.hstack(
                rx.text("Don't have an account?"),
                rx.link("Sign up", href="/auth/signup"),
                class_name="gap-2 justify-end w-full col-span-2",
            ),
        ),
    )


@rx.page(route="/auth/login")
def login() -> rx.Component:
    return ui.layout(content=login_card())

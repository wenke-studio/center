import reflex as rx
from sqlmodel import select

from center import layouts
from center.models import User

from .state import AuthState


class LoginState(AuthState):
    email: str
    password: str

    error: str

    def login(self):
        with rx.session() as session:
            user = session.exec(select(User).where(User.email == self.email)).first()
            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/")
            else:
                self.set_error("Invalid email or password")
                return


@layouts.landing_page
def login() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("Login"),
            rx.input(
                placeholder="Email",
                on_blur=LoginState.set_email,
            ),
            rx.input(
                placeholder="Password",
                on_blur=LoginState.set_password,
            ),
            rx.button("Login", on_click=LoginState.login),
            rx.cond(
                LoginState.error,
                rx.text(LoginState.error, class_name="text-red-500"),
            ),
        )
    )

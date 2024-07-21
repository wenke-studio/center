import reflex as rx
from sqlmodel import select

from center import layouts
from center.models import User

from .state import AuthState


class SignupState(AuthState):
    email: str
    password: str
    confirm_password: str

    error: str

    def signup(self):
        with rx.session() as session:
            if self.password != self.confirm_password:
                self.error = "Passwords do not match"
                return
            if session.exec(select(User).where(User.email == self.email)).first():
                self.error = "Email already exists"
                return
            self.user = User(email=self.email, password=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/auth/login")

    def on_mount(self) -> None:
        self.email = ""
        self.password = ""
        self.confirm_password = ""
        self.error = ""


@layouts.landing_page
def signup() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("Signup"),
            rx.input(
                placeholder="Email",
                on_blur=SignupState.set_email,
            ),
            rx.input(
                placeholder="Password",
                on_blur=SignupState.set_password,
            ),
            rx.input(
                placeholder="Confirm Password",
                on_blur=SignupState.set_confirm_password,
            ),
            rx.button("Signup", on_click=SignupState.signup),
            rx.hstack(
                rx.text("Already have an account?"),
                rx.link("Login", href="/auth/login"),
            ),
            rx.cond(
                SignupState.error,
                rx.text(SignupState.error, class_name="text-red-500"),
            ),
        ),
        on_mount=SignupState.on_mount,
    )

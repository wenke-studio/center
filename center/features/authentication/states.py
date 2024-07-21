from datetime import datetime, timezone

import reflex as rx
from sqlmodel import select

from .models import Token, User


class AuthState(rx.State):
    access_token: str = rx.LocalStorage(name="access-token")

    @rx.var(cache=True)
    def authenticated_user(self) -> User:
        """Get the authenticated user.

        If the user is not authenticated, return an anonymous user object (id=-1).

        Returns:
            User: The authenticated or anonymous user.
        """

        with rx.session() as session:
            statement = select(User, Token).where(
                User.id == Token.user_id,
                Token.client_token == self.access_token,
                Token.expired_at > datetime.now(timezone.utc),
            )
            result = session.exec(statement).first()
            if result:
                user, _ = result
                return user
            return User(id=-1)  # anonymous user

    @rx.var(cache=True)
    def is_authenticated(self) -> bool:
        """Check if the user is authenticated.

        Returns:
            bool: True if the user is authenticated, False otherwise.
        """

        return self.authenticated_user.id >= 0

    def _logout(self, user_id: int) -> None:
        """Logout the user by deleting the token."""

        with rx.session() as session:
            statement = select(Token).where(Token.user_id == user_id)
            for token in session.exec(statement).all():
                session.delete(token)
            session.commit()

    def _login(self, user_id: int) -> None:
        """Login the user by creating a new token."""

        self._logout(user_id)
        self.access_token = self.router.session.client_token
        Token.create(user_id, self.access_token)


class RegisterState(AuthState):
    email: str
    password: str
    confirm_password: str
    error: str = ""

    def on_mount(self) -> None:
        self.email = ""
        self.password = ""
        self.confirm_password = ""
        self.error = ""

    def on_submit(self) -> rx.event.EventSpec | list[rx.event.EventSpec]:
        error_events = self._validate_fields()
        if error_events:
            return error_events
        User.create(self.email, self.password)
        return rx.redirect("/auth/login")

    def _validate_fields(self) -> rx.event.EventSpec | list[rx.event.EventSpec] | None:
        if not self.email:
            self.error = "Email is required"
            return (rx.set_focus("email"),)
        if not self.password:
            self.error = "Password is required"
            return rx.set_focus("password")
        if self.password != self.confirm_password:
            self.error = "Passwords do not match"
            return [
                rx.set_value("password", ""),
                rx.set_value("confirm_password", ""),
                rx.set_focus("password"),
            ]

        with rx.session() as session:
            statement = select(User).where(User.email == self.email)
            existing_user = session.exec(statement).one_or_none()
            if existing_user is not None:
                self.error = "Email is already taken"
                return [
                    rx.set_value("email", ""),
                    rx.set_value("password", ""),
                    rx.set_value("confirm_password", ""),
                    rx.set_focus("email"),
                ]
        self.error = ""


class LoginState(AuthState):
    email: str
    password: str
    error: str = ""

    def on_mount(self) -> None:
        self.email = ""
        self.password = ""
        self.error = ""

    def on_submit(self) -> rx.event.EventSpec | list[rx.event.EventSpec]:
        error_events = self._validate_fields()
        if error_events:
            return error_events
        with rx.session() as session:
            statement = select(User).where(
                User.email == self.email,
                User.password == User.hash_password(self.password),
            )
            existing_user = session.exec(statement).one_or_none()
            if existing_user:
                self._login(existing_user.id)
                return rx.redirect("/")
            else:
                self.error = "Invalid email or password"
                return [
                    rx.set_value("email", ""),
                    rx.set_value("password", ""),
                    rx.set_focus("email"),
                ]

    def _validate_fields(self) -> rx.event.EventSpec | list[rx.event.EventSpec] | None:
        if not self.email:
            self.error = "Email is required"
            return rx.set_focus("email")
        if not self.password:
            self.error = "Password is required"
            return rx.set_focus("password")
        self.error = ""


class LogoutState(AuthState):
    def on_submit(self) -> rx.event.EventSpec:
        self._logout(self.authenticated_user.id)
        self.reset()
        return rx.redirect("/auth/login")

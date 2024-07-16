from typing import Optional

import reflex as rx

from center.models import User


class AuthState(rx.State):
    """The base state for auth"""

    user: Optional[User] = None

    def logout(self):
        """
        log out a user
        """
        self.reset()
        return rx.redirect("/")

    def guard(self):
        """
        redirect to login page if user is not logged in
        """
        if not self.logged_in:
            return rx.redirect("/auth/login")

    @rx.var
    def logged_in(self):
        """
        return if user is logged in
        """
        return self.user is not None

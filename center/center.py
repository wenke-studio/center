import reflex as rx

from center import (
    models,  # noqa
    pages,
)
from center.pages.auth.state import AuthState

app = rx.App()


app.add_page(pages.home, route="/", on_load=AuthState.guard)
app.add_page(pages.discover, route="/discover", on_load=AuthState.guard)
app.add_page(pages.sponsorship, route="/sponsorship", on_load=AuthState.guard)
# auth pages
app.add_page(pages.auth.signup, route="/auth/signup")
app.add_page(pages.auth.login, route="/auth/login")

# rx.Model.migrate()

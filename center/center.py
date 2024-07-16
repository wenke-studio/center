import reflex as rx

from center import (
    models,  # noqa
    pages,
)

app = rx.App()


app.add_page(pages.home, route="/")
app.add_page(pages.discover, route="/discover")
app.add_page(pages.sponsorship, route="/sponsorship")

# rx.Model.migrate()

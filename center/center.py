import reflex as rx

from center import pages

app = rx.App()


app.add_page(pages.home, route="/")

import reflex as rx

from center import pages  # noqa
from center.features.api import service

app = rx.App(
    style={
        ".debug": {
            "border": "1px solid red",
        }
    }
)

app.api.include_router(service)

import reflex as rx

from center import pages  # noqa
from center.features.api import service

app = rx.App()

app.api.include_router(service)

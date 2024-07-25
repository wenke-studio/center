import reflex as rx

from center.backend.service import router
from center.frontend import pages  # noqa

app = rx.App()

app.api.include_router(router)

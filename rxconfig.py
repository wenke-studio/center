import reflex as rx

config = rx.Config(
    app_name="center",
    db_url="sqlite:///reflex.db",
    # Disable React Strict Mode to debug lifecycle on production
    # https://github.com/reflex-dev/reflex/issues/3382
    # react_strict_mode=False,
)

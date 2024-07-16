import reflex as rx
from sqlmodel import Field


class User(rx.Model, table=True):
    """User Table"""

    email: str = Field(unique=True)
    password: str

    # Metadata
    username: str = ""

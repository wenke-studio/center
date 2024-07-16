from __future__ import annotations

from enum import Enum
from typing import List, Optional

import reflex as rx
from sqlmodel import Field, Relationship


class User(rx.Model, table=True):
    """User Table"""

    email: str = Field(unique=True)
    password: str

    # Metadata
    username: str = ""

    # Relationships
    services: List[Service] = Relationship(back_populates="user")


class ServiceStatus(Enum):
    active = "active"
    inactive = "inactive"


class ServiceCurrency(Enum):
    USD = "USD"
    TWD = "TWD"


class Service(rx.Model, table=True):
    """Service Table"""

    user_id: int = Field(foreign_key="user.id")

    name: str

    status: str = Field(default=ServiceStatus.active)
    plan: str
    amount: float
    currency: str = Field(default=ServiceCurrency.USD)
    billing_cycle: Optional[str] = Field(default="monthly")

    # Relationships
    user: User = Relationship(back_populates="services")

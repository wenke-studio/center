from enum import Enum
from typing import Optional

import reflex as rx
from sqlmodel import Field, Relationship

from center.features.authentication.models import User


class ServiceStatus(Enum):
    active = "active"
    inactive = "inactive"


class ServiceCurrency(Enum):
    USD = "USD"
    TWD = "TWD"


class Service(rx.Model, table=True):
    """Service Table"""

    name: str

    status: str = Field(default=ServiceStatus.active)
    plan: str
    amount: float
    currency: str = Field(default=ServiceCurrency.USD)
    billing_cycle: Optional[str] = Field(default="monthly")

    # Relationships
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="services")

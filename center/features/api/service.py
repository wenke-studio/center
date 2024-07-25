import json
from typing import List

import reflex as rx
from fastapi import APIRouter, Request
from pydantic import BaseModel
from sqlmodel import select

from center.features.api.models import Service


class Srv(BaseModel):
    """A temporary serializer for Service model

    Reflex is still using Pydantic V1, which causes an error in FastAPI
    when serializing the Service model in the swagger document

    # fixme: use Service model instead of this, when Reflex is updated to Pydantic V2
    """

    id: int
    name: str
    plan: str


class OK(BaseModel):
    message: str


async def list_services(req: Request) -> List[Srv]:
    with rx.session() as session:
        statement = select(Service).where(
            Service.user_id == req.user_id,
        )
        return session.exec(statement).all()


async def create_service(req: Request) -> OK:
    data = json.loads(await req.body())
    with rx.session() as session:
        session.add(Service(**data))
        session.commit()
    return OK(message="OK")


async def retrieve_service(user_id: int, service_id: int) -> Srv:
    with rx.session() as session:
        statement = select(Service).where(
            Service.user_id == user_id,
            Service.id == service_id,
        )
        return session.exec(statement).one_or_none()


async def update_service(user_id: int, req: Request) -> OK:
    data = json.loads(await req.body())
    with rx.session() as session:
        session.add(
            Service(
                **data,
                uesr_id=user_id,
            )
        )
        session.commit()
    return OK(message="OK")


async def destroy_service(user_id: int, service_id: int) -> OK:
    with rx.session() as session:
        statement = select(Service).where(
            Service.user_id == user_id,
            Service.id == service_id,
        )
        session.exec(statement).delete()
        session.commit()
    return OK(message="OK")


router = APIRouter(prefix="/service", tags=["service"])

router.add_api_route("/", list_services, methods=["GET"])
router.add_api_route("/", create_service, methods=["POST"])
router.add_api_route("/{service_id}", retrieve_service, methods=["GET"])
router.add_api_route("/{service_id}", update_service, methods=["PUT"])
router.add_api_route("/{service_id}", destroy_service, methods=["DELETE"])

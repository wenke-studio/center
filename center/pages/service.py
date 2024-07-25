import reflex as rx
from sqlmodel import select

from center import layouts
from center.features.api.models import Service
from center.features.authentication import AuthState, login_required


class ServiceState(AuthState):
    def on_load(self) -> rx.event.EventSpec | None:
        if not self.is_authenticated:
            return rx.redirect("/auth/login")

    @rx.var(cache=True)
    def whoami(self):
        return f"{self.authenticated_user.id} {self.authenticated_user.email}"

    services: list[Service] = []

    def list_services(self) -> None:
        with rx.session() as session:
            statement = select(Service).where(Service.user_id == self.authenticated_user.id)
            results = session.exec(statement).all()
            self.services = results or []

    @rx.var
    def total_services(self) -> int:
        return len(self.services)

    def create_service(self) -> rx.event.EventSpec:
        with rx.session() as session:
            session.add(
                Service(
                    name="service1",
                    status="active",
                    plan="plan1",
                    amount=100.0,
                    currency="USD",
                    billing_cycle="monthly",
                    user_id=self.authenticated_user.id,
                )
            )
            session.commit()
        return ServiceState.list_services

    def destroy_service(self, service_id: int) -> rx.event.EventSpec:
        with rx.session() as session:
            statement = select(Service).where(Service.id == service_id)
            service = session.exec(statement).one_or_none()
            if service:
                session.delete(service)
                session.commit()
        return ServiceState.list_services


@rx.page(route="/service", on_load=ServiceState.on_load)
@layouts.dashboard
@login_required
def service():
    return rx.box(
        rx.heading("Service"),
        rx.text(ServiceState.whoami),
        rx.button(
            "create a fake service",
            on_click=ServiceState.create_service,
        ),
        rx.vstack(
            rx.foreach(
                ServiceState.services,
                lambda service: rx.hstack(
                    rx.text(service.id),
                    rx.text(service.name),
                    rx.button(
                        "delete me",
                        on_click=lambda: ServiceState.destroy_service(service.id),
                    ),
                ),
            ),
            class_name="gap-4",
            on_mount=ServiceState.list_services,
        ),
    )

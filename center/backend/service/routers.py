from fastapi import APIRouter

from . import views

router = APIRouter(prefix="/service", tags=["service"])

router.add_api_route("/", views.list_services, methods=["GET"])
router.add_api_route("/", views.create_service, methods=["POST"])
router.add_api_route("/{service_id}", views.retrieve_service, methods=["GET"])
router.add_api_route("/{service_id}", views.update_service, methods=["PUT"])
router.add_api_route("/{service_id}", views.destroy_service, methods=["DELETE"])

from rest_framework.routers import DefaultRouter
from goNetwork.api.views import UbicationViewSet

router_ubication = DefaultRouter()
router_ubication.register(
    prefix='ubication',
    basename='ubication',
    viewset=UbicationViewSet
    )
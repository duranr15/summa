from rest_framework.routers import DefaultRouter
from goNetwork.api.views import SedeViewSet,DeviceViewSet

router_sede = DefaultRouter()
router_sede.register(
    prefix='sede',
    basename='sede',
    viewset=SedeViewSet
    )

router_device = DefaultRouter()
router_device.register(
    prefix='device',
    basename='device',
    viewset=DeviceViewSet
    )
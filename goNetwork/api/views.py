from goNetwork.models import Sede, Device
from rest_framework import viewsets
from rest_framework import permissions
from goNetwork.api.serializers import SedeSerializer, DeviceSerializer


class SedeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sede.objects.all().order_by('id')
    serializer_class = SedeSerializer
    #permission_classes = [permissions.IsAuthenticated]

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer
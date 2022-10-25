from goNetwork.models import Ubication
from rest_framework import viewsets
from rest_framework import permissions
from goNetwork.api.serializers import UbicationSerializer


class UbicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ubication.objects.all().order_by('id')
    serializer_class = UbicationSerializer
    #permission_classes = [permissions.IsAuthenticated]
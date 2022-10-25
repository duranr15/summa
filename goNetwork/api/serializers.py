from goNetwork.models import Ubication
from rest_framework import serializers


class UbicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubication
        fields = ['country', 'company', 'business', 'sede','type']


   
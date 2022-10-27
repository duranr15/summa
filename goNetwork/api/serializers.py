from goNetwork.models import Sede, Device
from rest_framework import serializers

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['sede', 'site', 'hostname']

class SedeSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True)
    
    class Meta:
        model = Sede
        fields = ['country', 'company', 'business', 'name','type_sede', 'devices']

    def create(self, validated_data):
        device_data = validated_data.pop('devices')
        sede = Sede.objects.create(**validated_data)
        for device_data in device_data:
            Sede.objects.create(sede=sede, **device_data)
        return sede
    
    

   
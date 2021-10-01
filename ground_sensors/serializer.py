from rest_framework import serializers
from ground_sensors.models import GroundSensor


class GroundSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundSensor
        fields = '__all__'

from rest_framework import viewsets
from ground_sensors.models import GroundSensor
from ground_sensors.serializer import GroundSensorSerializer


class GroundSensorViewSet(viewsets.ModelViewSet):
    """Displays data from ground sensors"""

    queryset = GroundSensor.objects.all()

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        return GroundSensorSerializer

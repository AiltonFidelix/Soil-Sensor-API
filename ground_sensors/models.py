from django.db import models


class GroundSensor(models.Model):
    """Model from ground sensor API"""

    device = models.CharField(max_length=10, primary_key=True)
    soil_humidity = models.IntegerField()
    air_humidity = models.IntegerField()
    temperature = models.FloatField()
    battery_life = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device

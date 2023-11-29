from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(null=True, blank=True)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)



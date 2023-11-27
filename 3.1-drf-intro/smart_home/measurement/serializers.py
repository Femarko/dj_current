from rest_framework import serializers
from .models import Sensor
# TODO: опишите необходимые сериализаторы
class SensorSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

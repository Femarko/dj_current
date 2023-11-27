# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor
from .serializers import SensorSerialaizer

@api_view(['GET'])
def list_sensors(request):
    sensors = Sensor.objects.all()
    serializer = SensorSerialaizer(sensors, many=True)
    return Response(serializer.data)

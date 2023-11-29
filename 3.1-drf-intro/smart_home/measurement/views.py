# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerialaizer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

    def post(self, request):
        entry = Sensor(name=request.data.get('name'), description=request.data.get('description'))
        entry.save()
        return Response({
            "entry created with the following id": entry.id,
            "new data": {
                "name": entry.name,
                "description": entry.description
            }
        })


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

    def patch(self, request, pk):
        entry = Sensor.objects.get(pk=pk)
        entry.name = request.data.get('name')
        entry.description = request.data.get('description')
        entry.save()
        return Response({
            "entry with the following id was modified": pk,
            "new data": {
                "name": entry.name,
                "description": entry.description
            }
        })

class CreateAPIView(APIView):
    def get(self, request):
        return Response({'status': 'OK'})
    def post(self, request):
        sensor = Sensor.objects.get(pk=request.data.get('sensor')).id
        entry = Measurement(sensor_id=sensor, temperature=request.data.get('temperature'))
        entry.save()
        return Response({
            "entry created with the following id": entry.id,
            "new data": {
                "sensor_id": entry.sensor_id,
                "temperature": entry.temperature
            }
        })

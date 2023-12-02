# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        entry = Sensor(name=request.data.get('name'), description=request.data.get('description'))
        entry.save()
        serialized_entry = SensorSerializer(entry)
        return Response(serialized_entry.data)

class RetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk): # обновление датчика
        entry = Sensor.objects.get(pk=pk)
        entry.name = request.data.get('name')
        entry.description = request.data.get('description')
        entry.save()
        serialized_entry = SensorSerializer(entry)
        return Response(serialized_entry.data)

    def get(self, request, pk): # получение информации по датчику
        serialized_entry = SensorDetailSerializer(Sensor.objects.get(pk=pk))
        print(Sensor.objects.get(pk=pk))
        print(serialized_entry.data)
        return Response(serialized_entry.data)


class CreateAPIView(APIView):
    def get(self, request):
        return Response({'status': 'OK'})
    def post(self, request):
        sensor = Sensor.objects.get(pk=request.data.get('sensor')) # так работает
        # а так:
        # sensor = Sensor.objects.get(pk=request.data.get('sensor')).id #- возвращается ошибка
        # "Cannot assign "1": "Measurement.sensor_id" must be a "Sensor" instance".
        entry = Measurement(sensor_id=sensor, temperature=request.data.get('temperature'))
        entry.save()
        serialized_entry = MeasurementSerializer(entry)
        return Response(serialized_entry.data)
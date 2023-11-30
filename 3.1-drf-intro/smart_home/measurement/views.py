# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

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
    serializer_class = SensorSerializer

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
        sensor = Sensor.objects.get(pk=request.data.get('sensor'))
        print(sensor)
        entry = Measurement(sensor_id=sensor, temperature=request.data.get('temperature'))
        entry.save()
        serialized_entry = MeasurementSerializer(entry)
        print(serialized_entry)
        # return Response({
        #     "entry created with the following id": entry.id,
        #     "new data": {
        #         "sensor_id": serialized_entry['sensor_id'],
        #         "temperature": entry.temperature
        #     }
        # })
        return Response(serialized_entry.data)

# class CreateAPIView(ListAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer
#
#     def post(self, request):
#         serializer = MeasurementSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

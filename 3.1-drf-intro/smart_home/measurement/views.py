# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
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

# class CreateAPIView(APIView): # перенес в качестве def post в class ListCreateAPIView(ListAPIView)
#     def post(self, request):
#         Sensor(name=request.data.get('name'), description=request.data.get('description')).save()
#         return Response({'status': 'OK'})

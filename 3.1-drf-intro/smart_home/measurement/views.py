# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .serializers import SensorSerialaizer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer


    class RetrieveUpdateAPIView(APIView):
        pass

class CreateAPIView(APIView):
    def post(self, request):
        Sensor(name=request.data.get('name'), description=request.data.get('description')).save()
        return Response({'status': 'OK'})

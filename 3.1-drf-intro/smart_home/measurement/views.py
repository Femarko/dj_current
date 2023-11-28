# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .serializers import SensorSerialaizer


class ListCreateAPIView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerialaizer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'status': 'OK'})
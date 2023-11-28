from django.urls import path
from measurement.views import ListCreateAPIView, CreateAPIView
urlpatterns = [
    path('', ListCreateAPIView.as_view()),
    path('sensor_create/', CreateAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]

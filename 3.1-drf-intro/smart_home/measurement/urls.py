from django.urls import path
from measurement.views import ListCreateAPIView, CreateAPIView
urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors_create/', CreateAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]

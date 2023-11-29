from django.urls import path
from measurement.views import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('measurements/', CreateAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]

from django.urls import path
from measurement.views import ListCreateAPIView, RetrieveUpdateAPIView
urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]

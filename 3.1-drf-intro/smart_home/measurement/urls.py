from django.urls import path
from measurement import views
urlpatterns = [
    path('sensor/', views.ListCreateAPIView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]

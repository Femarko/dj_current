from django.urls import path
from measurement import views
urlpatterns = [
    path('sensor/', views.list_sensors)
    # TODO: зарегистрируйте необходимые маршруты
]

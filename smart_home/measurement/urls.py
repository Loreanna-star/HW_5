from django.urls import path
from measurement.views import SensorView, UpdateSensor, CreateMeasurement

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
    
]

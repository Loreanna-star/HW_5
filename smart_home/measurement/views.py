from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement
from rest_framework.response import Response
from rest_framework import status

class SensorView(ListCreateAPIView):
    # получить список всех датчиков и создать новый
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
   
class UpdateSensor(RetrieveUpdateAPIView):
    # получить подробные данные по датчику
    # и обновить один датчик
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer
        else:
            return SensorSerializer   
    queryset = Sensor.objects.all()

class CreateMeasurement(CreateAPIView):
    # добавить измерение
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

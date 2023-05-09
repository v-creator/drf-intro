from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     RetrieveUpdateAPIView)

from .models import Measurement, Sensor
from .serializers import (AllSensorSerializer, MeasurementSerializer,
                          SensorSerializer)


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AllSensorSerializer


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

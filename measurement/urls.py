from django.urls import path

from measurement.views import MeasurementsView, SensorView, SingleSensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>', SingleSensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]

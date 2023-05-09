from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id_sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements',
        verbose_name='ID сенсора')
    temperature = models.FloatField(verbose_name='Температура')
    date_time = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерение температуры'
        verbose_name_plural = 'измерения температуры'
        ordering = ['-date_time']

    def __str__(self):
        return f'{self.id_sensor}, {self.temperature}, {self.date_time}'

from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    city = models.CharField(max_length=255, verbose_name='City')
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return f'{str(self.city)}(lat={self.latitude}, lon={self.longitude})'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cites'

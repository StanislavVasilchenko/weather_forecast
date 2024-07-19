from django.urls import path

from weather.apps import WeatherConfig
from weather.views import get_weather, CityDetailView

app_name = WeatherConfig.name

urlpatterns = [
    path('', get_weather, name='index'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]

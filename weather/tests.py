from unittest.mock import Mock

from django.test import TestCase

from weather.models import City
from weather.services import get_coordinates, get_weather_with_site
from weather.views import get_weather


class TestGetCoordinatesFunction(TestCase):
    def test_get_coordinates_valid_city(self):
        city_name = 'Москва'
        coordinates = get_coordinates(city_name)
        self.assertIsNotNone(coordinates)
        self.assertIn("latitude", coordinates)
        self.assertIn("longitude", coordinates)
        self.assertIn('timezone', coordinates)
        self.assertEqual(coordinates['city'], city_name)

    def test_get_coordinates_invalid_city(self):
        city_name = 'InvalidCityName'
        coordinates = get_coordinates(city_name)
        self.assertIsNone(coordinates)


class TestGetWeatherWithSiteFunction(TestCase):
    def test_get_weather_with_site_valid_coordinates(self):
        city_coordinates = {"latitude": 55.7558, "longitude": 37.6176, "city": "Moscow"}
        weather_data = get_weather_with_site(city_coordinates)
        self.assertIsNotNone(weather_data)
        self.assertIn("first_hour", weather_data)
        self.assertIn("second_hour", weather_data)
        self.assertIn("rain1", weather_data)
        self.assertIn("rain2", weather_data)

import requests

URL_BY_GET_GEO_CITY = 'https://geocoding-api.open-meteo.com/v1/search'
URL_BY_GET_WEATHER = 'https://api.open-meteo.com/v1/forecast'


def get_coordinates(city_name: str) -> dict | None:
    """Получение координат города по его названию возвращает словарь вида:
    "latitude": Широта,
    "longitude": Долгота,
    'timezone': Временная зона
    """
    response = requests.get(URL_BY_GET_GEO_CITY, params={'name': city_name})
    if response.json().get('results') is not None and response.status_code == 200:
        latitude = response.json()['results'][0].get('latitude')
        longitude = response.json()['results'][0].get('longitude')
        timezone = response.json()['results'][0].get('timezone')
        coordinates = {
            "latitude": latitude,
            "longitude": longitude,
            'timezone': timezone,
            'city': city_name
        }
        return coordinates
    return None


def get_weather_with_site(city_coordinates: dict) -> dict:
    """Принимает на вход координаты города.
    Получение температуры и кол-ва осадков на ближайшие два часа,
    возвращает словарь вида:
    'text_temp': Описание с названием города',
    'first_hour': Температура на текущий час,
    'second_hour': Температура на следующий час,
    'rain1': Количество осадков в первый час,
    'rain2': Количество осадков во второй час,
    """
    params = {'hourly': ['temperature_2m', 'rain'],
              'forecast_hours': 2
              }
    params.update(city_coordinates)
    response = requests.get(URL_BY_GET_WEATHER, params=params).json()
    context_data = {
        'first_hour': response['hourly']['temperature_2m'][0],
        'second_hour': response['hourly']['temperature_2m'][-1],
        'rain1': response['hourly']['rain'][0],
        'rain2': response['hourly']['rain'][-1],
    }
    return context_data

from django.shortcuts import render

from weather.services import get_weather_with_site, get_coordinates


def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        city_coordinates = get_coordinates(city)
        if city_coordinates is None:
            context_data = {'message': f"Город {city} не найден"}
            return render(request, 'weather/weather_result.html', context_data)
        context_data = get_weather_with_site(city_coordinates)
        return render(request, 'weather/weather_result.html', context_data)
    return render(request, 'weather/input_city_form.html')

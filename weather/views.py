from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from weather.models import City
from weather.services import get_weather_with_site, get_coordinates


@login_required(login_url='user/')
def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        city_coordinates = get_coordinates(city)
        if city_coordinates is None:
            context_data = {'message': f"Город {city} не найден"}
            return render(request, 'weather/weather_result.html', context_data)
        print(request.user)
        City.objects.create(city=city.capitalize(),
                            latitude=city_coordinates['latitude'],
                            longitude=city_coordinates['longitude'],
                            user=request.user)
        context_data = get_weather_with_site(city_coordinates)
        context_data['city'] = city.capitalize()
        return render(request, 'weather/weather_result.html', context_data)

    context_data = {'object_list': City.objects.filter(user=request.user).distinct('city')}
    return render(request, 'weather/input_city_form.html', context_data)


class CityDetailView(DetailView):
    model = City
    template_name = 'weather/weather_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        coordinates = {'latitude': self.object.latitude,
                       'longitude': self.object.longitude}
        context_data['object'] = get_weather_with_site(coordinates)
        return context_data

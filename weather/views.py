from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e3be2288352738837e4b2309e49ce1f2'
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types
        print(city_weather)

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data.__reversed__(), 'form': form}
    return render(request, 'index.html', context, )

def citywiki(request):
    return render(requests,'https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%BC%D0%B0-%D0%90%D1%82%D0%B0')
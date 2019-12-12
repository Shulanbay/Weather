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
    weather_data_clouds = ['few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds']
    weather_data_atmosphere = ['mist', 'Smoke', 'Haze', 'fog', 'sand/ dust whirls']
    weather_data_snow = ['light snow', 'Snow', 'Heavy snow', 'Sleet', 'Light shower sleet', 'Shower sleet', 'Light rain and snow', 'Rain and snow',
                         'Light shower snow', 'Shower snow', 'Heavy shower snow']
    weather_data_rain = ['light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain', 'extreme rain', 'freezing rain',
                         'light intensity shower rain', 'shower rain', 'heavy intensity shower rain', 'ragged shower rain']
    weather_data_clear = ['clear sky']
    weather_data_clothes = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
        print(city_weather)

        if city_weather['weather'][0]['description'] in weather_data_clouds:
            weather_data_clothes = 'Wear a Jacket'

        elif city_weather['weather'][0]['description'] in weather_data_clear:
            weather_data_clothes = 'Take a sunglasses'

        elif city_weather['weather'][0]['description'] in weather_data_atmosphere:
            weather_data_clothes = 'Be careful on the way'

        elif city_weather['weather'][0]['description'] in weather_data_rain:
            weather_data_clothes = 'Take an umbrella'

        elif city_weather['weather'][0]['description'] in weather_data_snow:
            weather_data_clothes = 'Dress warmly'
        else:
            weather_data_clothes = 'Stay at home'
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'clothes': weather_data_clothes
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data.__reversed__(), 'form': form}
    return render(request, 'index.html', context, )



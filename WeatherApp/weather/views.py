from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'a04af76800012410b1eccab687de9ab4'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&units=UTC&appid=" + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res["main"]['temp'],
            'feel': res["main"]['feels_like'],
            'wind': res["wind"]['speed'],
            'wind_deg': res['wind']['deg'],
            'grnd_level': res["main"]['pressure'],
            'humidity': res["main"]['humidity'],
            'sunrise': res["sys"]['sunrise'],
            'sunset': res["sys"]['sunset'],
            'icon': res["weather"][0]['icon'],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


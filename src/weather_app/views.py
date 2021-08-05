from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

from weather_app.models import City

# Create your views here.

def home_view(request):
    cities = City.objects.all()
    url = config("BASE_URL")
    # city = "Berlin"
    # r = requests.get(url.format(city))
    # "https://api.openweathermap.org/data/2.5/weather?q={}&appid=480221af134ea47c38f04b9244c0f45a".format("Berlin")
    # context = r.json()
    # pprint(context)

    city_data = []
    for city in cities:
        print(city)
        r = requests.get(url.format(city))
        content = r.json()
        pprint(content)
        data = {
            "city": city.name,
            "temperature": content["main"]["temp"],
            "description": content["weather"][0]["description"],
            "icon": content["weather"][0]["icon"]
        }
        city_data.append(data)

    print(city_data)
    context = {
        "city_data": city_data
    }
    return render(request, "weather_app/home.html", context)

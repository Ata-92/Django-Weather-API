from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

# Create your views here.

def home_view(request):
    url = config("BASE_URL")
    city = "Berlin"
    r = requests.get(url.format(city))
    # "https://api.openweathermap.org/data/2.5/weather?q={}&appid=480221af134ea47c38f04b9244c0f45a".format("Berlin")
    context = r.json()
    pprint(context)

    return render(request, "weather_app/home.html")

from django.urls import path

from weather_app.views import home_view

urlpatterns = [
    path("", home_view, name="home")
]

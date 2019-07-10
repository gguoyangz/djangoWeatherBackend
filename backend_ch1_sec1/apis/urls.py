from django.urls import path

from .views import weather, menu

urlpatterns = [
    # path('', weather.helloworld)
    # path('', weather.weather)
    path('weather', weather.weather),
    path('menu', menu.get_menu)
]
from django.shortcuts import render
from django.views import View
from .weather_rain import weather_rain_summ
from avto.counts import my_count


class Weather(View):

    @staticmethod
    def get(request):
        context = my_count()
        context.update(weather_rain_summ())
        return render(request, "weather.html", context)
import json
import requests

from django.shortcuts import render, HttpResponse

from .models import Vehicle


def first(request):
    vehicles = Vehicle.objects.all()
    context = {"vehicles": vehicles}
    return render(request, "app_dealer/index.html", context)


def content(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    return render(request, "app_dealer/content.html", {"vehicle": vehicle})


def weather(request):
    # url = "https://api.github.com/events"
    url = "https://api.open-meteo.com/v1/forecast?longitude=44.30&latitude=40.10&past_days=10&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    jdata = {"key": "value"}
    # data = requests.get(url)
    # data = requests.get(url).json()
    data = requests.get(url).json()
    # bl = data, data.raise_for_status()

    # return HttpResponse(json.loads("Hello"))
    return render(request, "app_dealer/weather.html", {"data": data})
    # return data

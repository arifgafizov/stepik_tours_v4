import random

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError

from tours.data import tours, departures, departure_tours, departures_list


class DepartureView(View):
    def get(self, request, departure):

        data = {"departure_city": departures[departure][3:],
                'departure_tours': departure_tours,
                'departure': departure,
                'departures': departures,
                'departure_count': departures_list[departure][0],
                'departure_min_price': min(departures_list[departure][1]),
                'departure_max_price': max(departures_list[departure][1]),
                'departure_min_nights': min(departures_list[departure][2]),
                'departure_max_nights': max(departures_list[departure][2])
                }
        return render(request, "tours/departure.html", context=data)


class TourView(View):
    def get(self, request, id):
        data = {'tours': tours[id], 'departures_id': departures[tours[id]['departure']], 'departures': departures}
        return render(request, 'tours/tour.html', context=data)


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {'random_list_id_tours': random.sample(range(1, 17), 6),'tours': tours, 'departures': departures})


def custom_handler404(request, exception):
    return HttpResponseNotFound("<h1>page not found</h1>")


def custom_handler500(request):
    return HttpResponseServerError("<h1>server error</h1>")

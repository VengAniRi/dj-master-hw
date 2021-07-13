from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
from csv import DictReader
from urllib.parse import urlencode

def index(request):
    return redirect(reverse(bus_stations))


with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
    data = list(DictReader(csvfile))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))

    paginator = Paginator(data, settings.RECORDS_BY_PAGE)
    page_obj = paginator.get_page(current_page)
    stations = [{'Name': obj['Name'], 'Street': obj['Street'], 'District': obj['District']}
                    for obj in page_obj.object_list]
    current_page = page_obj.number
    next_page_url = None
    prev_page_url = None
    if page_obj.has_next():
        next_page_url = reverse('bus_stations') + '?' + urlencode({'page': current_page + 1})
    if page_obj.has_previous():
        prev_page_url = reverse('bus_stations') + '?' + urlencode({'page': current_page - 1})

    return render(request, 'index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


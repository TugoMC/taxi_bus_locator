from django.shortcuts import render
from .models import Stop
from django.db.models import Q

def stop_list(request):
    stops = Stop.objects.all()
    return render(request, 'stops/stop_list.html', {'stops': stops})

def stop_detail(request, pk):
    stop = Stop.objects.get(pk=pk)
    return render(request, 'stops/stop_detail.html', {'stop': stop})


def search_stops(request):
    query = request.GET.get('query')
    if query:
        stops = Stop.objects.filter(Q(name__icontains=query) | Q(commune__icontains=query))
    else:
        stops = Stop.objects.all()
    return render(request, 'stops/search_results.html', {'stops': stops, 'query': query})
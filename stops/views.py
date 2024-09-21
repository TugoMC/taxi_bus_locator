from django.shortcuts import render
from .models import Stop, LigneTrajet
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def stop_list(request):
    stops = Stop.objects.all()
    return render(request, 'stops/stop_list.html', {'stops': stops})

def search_stops(request):
    query = request.GET.get('query')
    if query:
        stops = Stop.objects.filter(Q(name__icontains=query) | Q(commune__icontains=query))
    else:
        stops = Stop.objects.all()
    return render(request, 'stops/search_results.html', {'stops': stops, 'query': query})

def stop_detail(request, pk):
    stop = Stop.objects.get(pk=pk)
    lignes = stop.lignes.all()  # Récupérer les lignes associées à cet arrêt
    return render(request, 'stops/stop_detail.html', {'stop': stop, 'lignes': lignes, 'user': request.user})

@csrf_exempt
def creer_ligne(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        trajet_id = data.get('stop_id')
        points = data.get('points')
        debut_nom = data.get('debut_nom', "Début")
        fin_nom = data.get('fin_nom', "Fin")

        stop = Stop.objects.get(id=trajet_id)
        ligne = LigneTrajet.objects.create(
            stop=stop,
            points=points,
            debut_nom=debut_nom,
            fin_nom=fin_nom
        )
        
        return JsonResponse({'id': ligne.id, 'stop_id': stop.id, 'points': points, 'debut_nom': debut_nom, 'fin_nom': fin_nom})
    return JsonResponse({'error': 'Invalid request'}, status=400)

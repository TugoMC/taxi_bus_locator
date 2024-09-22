from django.shortcuts import render
from .models import Stop, LigneTrajet
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404


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
        try:
            data = json.loads(request.body)
            trajet_id = data.get('stop_id')
            points = data.get('points')
            stop = Stop.objects.get(id=trajet_id)
            
            ligne = LigneTrajet.objects.create(
                stop=stop,
                points=points
            )
            
            return JsonResponse({'id': ligne.id, 'stop_id': stop.id, 'points': points})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@user_passes_test(lambda u: u.is_superuser)
def delete_ligne(request, ligne_id):
    if request.method == 'POST':
        ligne = get_object_or_404(LigneTrajet, id=ligne_id)
        ligne.delete()  # Supprimer la ligne
        return JsonResponse({'status': 'success', 'message': 'Ligne supprimée avec succès.'})
    
    return JsonResponse({'error': 'Requête non valide.'}, status=400)
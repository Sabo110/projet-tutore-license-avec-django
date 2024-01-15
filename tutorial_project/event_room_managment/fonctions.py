from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json

from .models import Reservation

@csrf_exempt
@require_POST
def confirmer_ou_annuler_une_reservation(request, id_reservation):
    try:
        #on recupere la reservation a partir de son id
        reservation = Reservation.objects.get(id=id_reservation)
        print(reservation)
        data = json.loads(request.body)
        print(data)
        #on modifie la confirmation de la reservation en fonction de si l'utilisateur a confirme ou annule
        reservation.confirm_or_no = data.get('conf_ou_non')
        #on enregistre cela en bd
        reservation.pending = False
        reservation.save()
        # on renvoie une réponse JSON indiquant le succès
        return JsonResponse({'success': True})
            
    except Reservation.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'objet non trouvé'})
    except Exception as e:
        # on retourne une réponse JSON indiquant une erreur générale
        return JsonResponse({'success': False, 'message': str(e)})
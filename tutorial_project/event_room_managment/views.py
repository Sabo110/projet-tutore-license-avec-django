from django.shortcuts import render

# la fonction qui gere l'affichage de la page d'accueil ou home page
def home_page(request):
    return render(request, 'event_room_managment/home_page.html')

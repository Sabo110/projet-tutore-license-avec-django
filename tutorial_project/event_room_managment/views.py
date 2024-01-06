from django.shortcuts import render

# la fonction qui gere l'affichage de la page d'accueil ou home page
def home_page(request):
    return render(request, 'event_room_managment/home_page.html')

# la fonction qui gere l'affichage de la page membre ou member page
def member_page(request):
    return render(request, 'event_room_managment/member_page.html')

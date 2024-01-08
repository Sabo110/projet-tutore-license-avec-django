from django.shortcuts import render

# la fonction qui gere l'affichage de la page d'accueil ou home page
def home_page(request):
    return render(request, 'event_room_managment/home_page.html')

# la fonction qui gere l'affichage de la page membre ou member page
def member_page(request):
    return render(request, 'event_room_managment/member_page.html')

# fonction qui affiche l'affichage du profil de l'utilisateur ie nom , date de naissance ...
def profile(request):
    return render(request, 'event_room_managment/profile.html')

# fonction qui affiche le détail sur une réservation
def detail(request):
    return render(request, 'event_room_managment/detail.html')

 # fonction qui affiche la page de demande d'une réservation
def demande(request):
    return render(request, 'event_room_managment/demande.html')   
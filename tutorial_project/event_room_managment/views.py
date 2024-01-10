from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.urls import reverse_lazy


from .models import Room, Picture
from .forms import RoomForm


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

# fonction qui affiche la page de réservation
def reservation(request):
    return render(request, 'event_room_managment/reservation.html')   

# fonction qui affiche la page room detail
def room_detail(request):
    return render(request, 'event_room_managment/room_detail.html')   

# la classe qui va gerer la creation d'une sale
class CreateRoom(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'event_room_managment/create_room.html'
    success_url = reverse_lazy('create_room')

    # la methode qui est execute une fois le formualire soumit(ie apres le clic sur submit) et valide
    def form_valid(self, form):
        form.instance.owner = self.request.user # on lie l'instance de room qui sera cree a l'utilisateur connecte ie celui qui cree cette sale
        images = form.cleaned_data['images'] # on recupere la liste d'images selectionnees
        room = form.save()
        for image in images:
            Picture.objects.create(file=image, room=room)
        messages.success(self.request, "sale publié avec succès")
        return super().form_valid(form)

# la class qui gere l'affichage des sales(room)
class RoomList(ListView):
    model = Room
    template_name = 'event_room_managment/room_list.html'
    context_object_name = 'room_list' #le nom de la variable qui sera disponible dans le template pour afficher la liste de sales

    
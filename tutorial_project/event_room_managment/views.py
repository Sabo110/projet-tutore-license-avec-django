from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Room, Picture
from .forms import RoomForm, RoomFormUpdate, SearchRoomForm


# la fonction qui gere l'affichage de la page d'accueil ou home page
def home_page(request):
    return render(request, 'event_room_managment/home_page.html')

# la fonction qui gere l'affichage de la page membre ou member page
def member_page(request):
    # on verifie si l'utilisateur a soumis le formulaire
    if request.method == 'POST':
        # Associez le formulaire aux données POST
        form = SearchRoomForm(request.POST)
        # si le formulaire est valide
        if form.is_valid():
            #on recupere les donnees pour filtrer la recherche
            typ = form.cleaned_data.get('typ')
            daily_rate = form.cleaned_data.get('daily_rate')
            city = form.cleaned_data.get('city')
            neighborhood = form.cleaned_data.get('neighborhood')
            # on effectue la requete
            rooms = Room.objects.filter(typ=typ, city__icontains=city, neighborhood__icontains=neighborhood, daily_rate__lte=daily_rate)
    else:
        # on cree une instance du formulaire
        form = SearchRoomForm()
        rooms = []
   
    return render(request, 'event_room_managment/member_page.html', {'form': form, 'rooms': rooms})

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
        messages.success(self.request, "sale publié avec succès")# le message de succes qui sera affcihe une fois l'objet cree
        return super().form_valid(form)



#la fonction qui affiche les sales cree ou publie par un utilisateur(owner)
def RoomList(request):
    # on recupere l'utilisateur connecte
    user = request.user
    # on recupere ses sales
    room_list = user.sales.all()
    # on cree une pagination de 6 element par page
    paginator = Paginator(room_list, 6)
    # on recupere le numero de la page courante
    page_number = request.GET.get("page")
    # on recupere les elemnts de la page courante
    page_obj = paginator.get_page(page_number)
    return render(request, 'event_room_managment/room_list.html', {'page_obj': page_obj})



# la classe qui va gerer la modification d'une sale
class UpdateRoom(UpdateView):
    model = Room
    form_class = RoomFormUpdate
    template_name = 'event_room_managment/update_room.html'
    success_url = reverse_lazy('room_list')

    # la methode pour ajouter des valeurs au context
    def get_context_data(self, **kwargs: reverse_lazy):
        context = super().get_context_data(**kwargs)
        # on recupere le numero de la page dont l'objet a modifier provient
        num = self.request.GET.get('page', '1')
        context['num_page'] = num
        return context
    
    # la fonction qui va diriger l'utilisateur une fois la modification efectue avec succes
    def get_success_url(self) -> str:
        context = self.get_context_data() # on recupere le context
        num = context['num_page']
        url = reverse_lazy('room_list') # on genere l'url a aprtir du nom de l'url
        return f'{url}?page={num}'
                            
    # la methode qui est execute une fois le formualire soumit(ie apres le clic sur submit) et valide
    def form_valid(self, form):
        # on recupere les nouvelles images si l'utilisateur a uploadé de nouvelles
        images = form.cleaned_data['images']
        if images:
            # je recupere les anciennes images lie a cet objet
            anniennes_images = self.get_object().pictures.all()
            # on les supprimes
            for image in anniennes_images:
                image.delete()
            # on lie les nouvelles images a l'objet modifie
            for image in images:
                Picture.objects.create(file=image, room=self.object)
        messages.success(self.request, "sale modifié avec succès")
        return super().form_valid(form)



#la fonction pour supprimer une sale
def DeleteRoom(request, id):
    # on recupere le numero de la page d'ou provient l'objet a supprimer
    num_page = request.GET.get('page', '1')
    # je recupere l'objet a supprimer
    obj = get_object_or_404(Room, id=id)
    # je supprime l'objet
    obj.delete()
    # je cree le message de succes qui sera afficher a l'utilisateur une fois l'objet supprimé
    messages.success(request, f"sale {obj.city} - {obj.neighborhood} supprimé avec succès")
    url = reverse_lazy('room_list') + f'?page={num_page}' # on cree l'url 
    # je dirige vers l'url
    return redirect(url)





    
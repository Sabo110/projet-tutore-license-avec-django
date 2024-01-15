from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . import fonctions

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('members/', views.member_page, name='member_page'),
    path('profile/', views.profile, name='profile'),
    path('detail/', views.detail, name='detail'),
    path('demande/<int:id_room>/', views.demande, name='demande'),
    path('reservation/', views.reservation, name='reservation'),
    path('room/', views.room_detail, name='room_detail' ),
    path('create_room/', views.CreateRoom.as_view(), name='create_room'),
    path('room_list/', views.RoomList, name='room_list'),
    path('detele_room/<int:id>/', views.DeleteRoom, name='delete_room'),
    path('update_room/<int:pk>/', views.UpdateRoom.as_view(), name='update_room'),
    path('confir_or_no_reservation/<int:id_reservation>/', fonctions.confirmer_ou_annuler_une_reservation)
] 
# Servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
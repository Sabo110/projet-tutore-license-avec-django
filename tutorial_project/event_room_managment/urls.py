from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('members/', views.member_page, name='member_page'),
    path('profile/', views.profile, name='profile'),
    path('detail/', views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# l'ajout de ce parametre (+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)) permet l'affichage en front des fichiers statique comme les iamges
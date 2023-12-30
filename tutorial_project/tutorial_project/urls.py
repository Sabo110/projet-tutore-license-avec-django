
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentification/', include('authentification.urls')),
    path('', include('event_room_managment.urls'))
]

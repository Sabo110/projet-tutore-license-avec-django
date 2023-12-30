from django.urls import path, include

from . import views

urlpatterns = [
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path("accounts/", include("django.contrib.auth.urls")),
    
]

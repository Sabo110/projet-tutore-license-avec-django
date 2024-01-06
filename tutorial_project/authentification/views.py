from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout

from django.views import generic

from .models import CustomUser
from .forms import SignUpForm

# la classe qui gere l'inscription des utilisateurs
class SignUp(generic.CreateView):
    model = CustomUser # le model de creation d'instance d'utilisateur
    form_class = SignUpForm # le formulaire d'inscription
    template_name = 'authentification/sign_up.html' # le template sur lequel le formulaire sera rendu
    success_url = reverse_lazy('login') # en cas de succes l'utilisateur sera dirige vers la page de login
    


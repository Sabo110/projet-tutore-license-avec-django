from django.shortcuts import render
from django.views import generic

from .models import CustomUser
from .forms import SignUpForm

class SignUp(generic.CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'authentification/sign_up.html'


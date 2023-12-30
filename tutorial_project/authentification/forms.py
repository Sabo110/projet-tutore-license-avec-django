from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'email','city', 'neighborhood', 'account_type', 'phone_number', 'password1', 'password2']
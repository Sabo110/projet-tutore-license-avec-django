from django.db import models
from django.contrib.auth.models import AbstractUser

from event_room_managment.models import Adress

# creons un models qui va etendre le models user de base de django
class CustomUser(AbstractUser, Adress):
    choices = [
        ('client', 'Client'),
        ('owner', 'Owner'),
    ]
    date_of_birth = models.DateField(null=True, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    account_type = models.CharField(max_length=10, choices=choices, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)# la date a laquelle le compte a ete cree
    updated_at = models.DateTimeField(auto_now=True)# la date de modification la plus recente d'une ou plusieurs informations du compte(password ou autre)
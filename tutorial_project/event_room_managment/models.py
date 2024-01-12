from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# creons notre classe abstraite adress
class Adress(models.Model):
    city = models.CharField(max_length=20, null=True, blank=False) #la ville
    neighborhood = models.CharField(max_length=20, null=True, blank=False) #le quartier

    class Meta:
        abstract = True
    
class Room(Adress):
    choices = [
        ('mariage', 'Mariage'),
        ('anniversaire', 'Anniversaire'),
        ('conference', 'Conference'),
        ('reunion', 'Reunion'),
        ('ceremonie', 'Ceremonie'),
    ]
    description = models.TextField(null=True, blank=True)
    daily_rate = models.PositiveIntegerField(null=False, blank=False) # le prix journalier
    typ = models.CharField(max_length=20, choices=choices, null=False, blank=False) # le type de sale (mariage, anniversaire ...)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales')

class Picture(models.Model):
    file = models.ImageField(upload_to='images_de_sale')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='pictures')

class Reservation(models.Model):
    reservation_date = models.DateTimeField(auto_now_add=True)
    begin_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    pending = models.BooleanField(default=False) # en attente
    confirm_or_no = models.BooleanField(null=True) # confirmé ou non
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')

# on ecouteurs d'evenement sur la suppression d'une instance du model picture
@receiver(post_delete, sender=Picture)
def gestionnaire_post_delete_image(sender, instance, **kwargs):
    # Cette fonction sera appelée après que l'objet Image a été supprimé de la base de données.

    # on supprime l'image dans le dossier physique de l'application
    os.remove(os.path.join(settings.MEDIA_ROOT, instance.file.name))#instance.file.name : contient le chemin de l'image dans la bd

    
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type_choices = [
        ('particular', 'Particular'),
        ('empresa', 'Empresa'),
        ('administrador', 'Administrador'),
    ]
    user_type = models.CharField(max_length=15, choices=user_type_choices)
   # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Space(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,unique=True)
    capacity = models.IntegerField(default=1)
    description = models.TextField(max_length=300, blank=True,null=True, default='Sin Descripcion')
    price_per_hour = models.FloatField(default=0.1)
   # space_picture = models.ImageField(upload_to='space_pictures/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador')

    def __str__(self):
        return self.name
 
 class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='espacio')
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    start_datetime = models.DateTimeField(editable=True, blank=False, null=False)
    end_datetime = models.DateTimeField(editable=True, blank=False, null=False)
    status_choices = [
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
        ('en espera', 'En espera')
    ]
    status=models.CharField(max_length=15, choices=status_choices, default='en espera')

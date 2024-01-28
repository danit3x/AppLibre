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

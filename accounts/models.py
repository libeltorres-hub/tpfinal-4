from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    link = models.URLField(blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

from django.db import models
from django.contrib.auth.models import User

class Metatraders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    ip_address = models.CharField(max_length=50, blank=True)
    port = models.CharField(max_length=10, blank=True)
    token = models.CharField(max_length=100, blank=True)

    def is_token_filled(self):
        return bool(self.token)

    def __str__(self):
        return self.user.username

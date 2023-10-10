from django.db import models
from django.contrib.auth.models import User
from settingsApp.models import Account  # Import model Account dari settingsApp

# Definisikan model lain di profileApp jika ada
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)  # Gunakan model Account di sini
    profile_image = models.ImageField(upload_to='profile_images/', default='default.jpg', blank=True, null=True)
    # Tambahkan field lain yang Anda butuhkan

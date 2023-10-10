from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # Import modul Pillow

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.CharField(max_length=100, default="Write Your Bio...", null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='images/')

    def __str__(self):
        return self.user.username

    # Override save method to resize profile image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_image and self.profile_image != 'default.jpg':
            img = Image.open(self.profile_image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_image.path)

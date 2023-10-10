from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200,blank=True, null=True)
    speaker = models.CharField(max_length=100,blank=True, null=True)  # Field pengisi acara
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Field gambar

    def __str__(self):
        return self.title

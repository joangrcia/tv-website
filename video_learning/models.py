# video_learning/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)  # Menambahkan deskripsi video
    categories = models.ManyToManyField(Category)
    image = models.ImageField(null=True, blank=True, default='default_thumb.jpg', upload_to='video_images/')
    slug = models.SlugField(blank=True, editable=False)
    
    def jumlah_episode(self):
        return self.season_set.aggregate(models.Count('episode'))['episode__count']  # Menghitung jumlah episode
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Panggil fungsi resize_image untuk mengompres gambar saat disimpan
        self.resize_image()

    def resize_image(self):
        if self.image:
            img = Image.open(self.image.path)

            # Ubah ukuran gambar sesuai kebutuhan Anda
            max_size = (800, 600)
            img.thumbnail(max_size)
            img.save(self.image.path)
    
    def __str__(self):
        return self.title

class Season(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    season_number = models.IntegerField()
    
    # tambahkan bidang lain sesuai kebutuhan

    def __str__(self):
        return f"{self.video.title} - Season {self.season_number}"

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.IntegerField(blank=True, null=True)  # Menambahkan URL video
    description = models.TextField(default="", blank=True, null=True)  # Menambahkan deskripsi episode
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Panggil fungsi resize_image untuk mengompres gambar saat disimpan
        self.resize_image()

    def resize_image(self):
        if self.image:
            img = Image.open(self.image.path)

            # Ubah ukuran gambar sesuai kebutuhan Anda
            max_size = (800, 600)
            img.thumbnail(max_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.season.video.title} - Season {self.season.season_number} - Episode {self.title}"

class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    proof_of_payment = models.ImageField(upload_to='proofs/')
    is_validated = models.BooleanField(default=False)
    # tambahkan bidang lain sesuai kebutuhan

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"
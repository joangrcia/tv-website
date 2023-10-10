from django.db import models
from django.contrib.auth.models import User
import hashlib
import hmac
import asyncio
from ckeditor.fields import RichTextField
from django.conf import settings
from telegram import Bot
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    MQL_CHOICES = [
        ('mql4', 'MQL4'),
        ('mql5', 'MQL5'),
        ('book', 'BOOK'),
    ]
    title = models.CharField(max_length=200)
    product_type = models.CharField(max_length=4, choices=MQL_CHOICES, default='mql4')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    version = models.CharField(max_length=20)
    last_update = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = RichTextField()
    photo = models.ImageField(upload_to='product_photos/')
    file = models.FileField(upload_to='product_files/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_purchased = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Panggil fungsi resize_image untuk mengompres gambar saat disimpan
        self.resize_image()

    def resize_image(self):
        if self.photo:
            img = Image.open(self.photo.path)

            # Ubah ukuran gambar sesuai kebutuhan Anda
            max_size = (826, 1169)
            img.thumbnail(max_size)
            img.save(self.photo.path)


    def __str__(self):
        return self.title

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mt_name = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, editable=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    proof_of_payment = models.FileField(upload_to='proof_of_payments/', blank=True, null=True)  # Menambahkan field proof_of_payment

    def generate_combined_hash(self, key, message):
        key = bytes(key, 'utf-8')
        message = bytes(message, 'utf-8')
        return hmac.new(key, message, hashlib.sha256).hexdigest()
    
    async def send_telegram_notification(self):
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = '-1001746431842'  # Ganti dengan ID obrolan Anda

        bot = Bot(token=bot_token)
        message = f"Pembelian baru oleh {self.user.username} - Produk: {self.product.title}"
        await bot.send_message(chat_id=chat_id, text=message)

    def save(self, *args, **kwargs):
        if self.mt_name:
            if self.product:
                self.token = self.generate_combined_hash(self.product.title, self.mt_name)
                asyncio.run(self.send_telegram_notification())  # Panggil fungsi async menggunakan asyncio.run()
        super(Purchase, self).save(*args, **kwargs)



    def __str__(self):
        return f"{self.user.username} purchased {self.product.title}"

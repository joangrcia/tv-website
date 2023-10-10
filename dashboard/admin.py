from django.contrib import admin
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at')

admin.site.register(Ad, AdAdmin)

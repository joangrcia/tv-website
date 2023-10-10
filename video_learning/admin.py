# video_learning/admin.py

from django.contrib import admin
from .models import Video, Season, Episode, Category

class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SeasonInline]
    readonly_fields = ['slug',]

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('video', 'season_number')
    inlines = [EpisodeInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('season', 'title')
    readonly_fields = ['slug',]

admin.site.register(Video, VideoAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Category, CategoryAdmin)  # Mendaftarkan model Category di halaman admin
admin.site.register(Episode, EpisodeAdmin)

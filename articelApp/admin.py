from django.contrib import admin
from .models import Blog, Category, Comment,Viewer

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Viewer)

from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth.views import LogoutView

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.indexLogout, name='logout'),
]

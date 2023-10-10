from django.urls import path
from . import views

app_name = "articel"

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('detail/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('category/<str:category>/', views.blog_list, name='blog_list_by_category'),
 
]

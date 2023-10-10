from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('products/<str:category_name>/<str:product_type>/', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/purchase/', views.purchase_product, name='purchase_product'),
    path('my-products/', views.my_products, name='my_products'),
    path('product/<int:product_id>/payment/', views.payment, name='payment'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('product/<int:product_id>/download/', views.download_product, name='download_product'),
]

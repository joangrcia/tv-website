from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Product, Purchase, Category
from django.contrib.auth.decorators import login_required
import os
from .forms import PaymentForm  # Import PaymentForm dari forms.py
import hashlib
from django.http import JsonResponse

@login_required
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    category_filter = request.GET.get('category')
    product_type_filter = request.GET.get('product_type')
    price_filter = request.GET.get('price_filter')  # Ambil filter harga

    if category_filter:
        category = get_object_or_404(Category, name=category_filter)
        products = products.filter(category=category)

    if product_type_filter:
        products = products.filter(product_type=product_type_filter)

    # Terapkan filter harga
    if price_filter == 'free':
        products = products.filter(price=0)  # Filter produk gratis
    elif price_filter == 'paid':
        products = products.exclude(price=0)  # Filter produk berbayar

    return render(request, 'productapp/product_list.html', {'products': products, 'categories': categories})



@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    is_purchased = Purchase.objects.filter(user=request.user, product=product, is_confirmed=True).exists()
    return render(request, 'productapp/product_detail.html', {'product': product, 'is_purchased': is_purchased})

@login_required
def purchase_product(request, product_id):
    return redirect('product:product_detail', product_id=product_id)

@login_required
def my_products(request):
    purchased_products = Purchase.objects.filter(user=request.user, is_confirmed=True)
    return render(request, 'productapp/my_products.html', {'purchased_products': purchased_products})

@login_required
def payment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            proof_of_payment = form.cleaned_data['proof_of_payment']
            mt_name = form.cleaned_data['mt_name']  # Ambil mt_name dari formulir
            
            # Selanjutnya, Anda dapat membuat instance Purchase baru dengan bukti transfer dan mt_name yang diunggah
            purchase = Purchase(user=request.user, product=product, mt_name=mt_name, proof_of_payment=proof_of_payment)
            purchase.save()
            return redirect('product:confirmation')
    else:
        form = PaymentForm()
    
    return render(request, 'productapp/payment.html', {'product': product, 'form': form})


@login_required
def confirmation(request):
    # Pastikan untuk mengganti 'purchase_list' dengan objek atau data yang sesuai dalam model Anda.
    purchase_list = Purchase.objects.filter(user=request.user, is_confirmed=True)
    
    # Jika ada pembelian yang telah dikonfirmasi, arahkan pengguna ke halaman "My Produk"
    if purchase_list.exists():
        return redirect('product:my_products')
    
    return render(request, 'productapp/confirmation.html', {'purchase_list': purchase_list})


@login_required
def download_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Mengambil ekstensi berkas dari nama berkas yang diunggah
    file_name, file_extension = os.path.splitext(product.file.name)
    
    with open(product.file.path, 'rb') as file:
        response = HttpResponse(file.read())
        response['Content-Disposition'] = f'attachment; filename="{product.title}{file_extension}"'
        return response

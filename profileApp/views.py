from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from settingsApp.models import Account
from articelApp.models import Blog  # Impor model Blog

@login_required
def index(request):
    try:
        account = Account.objects.get(user=request.user)  # Ambil data Account yang terkait dengan pengguna saat ini
    except Account.DoesNotExist:
        account = None

    # Ambil daftar artikel terbaru
    articles = Blog.objects.order_by('-date')[:3]  # Mengambil 5 artikel terbaru

    context = {
        "judul": "Ini adalah halaman profil",
        "account": account,
        "articles": articles,  # Sertakan daftar artikel ke dalam konteks
    }
    return render(request, "profileApp/index.html", context)

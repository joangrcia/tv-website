from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Ad

@login_required
def index(request):
    ads = Ad.objects.order_by('-created_at')[:2]
    context = {
        'title':'TraderVibes',
        'judul':'Selamat Datang',
        'subheading':'di TraderVibes',
        'ads': ads,
    }
    return render(request, 'dashboard/index.html', context)

def indexLogout(request):
    logout(request)
    return redirect('indexlogout')

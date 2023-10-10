from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account
from .forms import EditProfileForm

@login_required
def index(request):
    try:
        account = request.user.account
    except Account.DoesNotExist:
        account = Account.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            account.user_bio = form.cleaned_data['user_bio']
            account.profile_image = form.cleaned_data['profile_image']
            account.save()
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        initial_data = {
            'user_bio': account.user_bio,
        }
        form = EditProfileForm(instance=request.user, initial=initial_data)
        
    context = {
        "judul": "ini adalah halaman calender",
        'form': form,
    }
    return render(request, "settingsApp/index.html", context)

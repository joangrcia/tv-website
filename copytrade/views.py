from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from .models import Metatraders
from .forms import MetatraderForm
from django.contrib.auth.decorators import login_required

@login_required
def connect_to_mt5(login, password, host, port):
    url = f"https://mt5.mtapi.be/Connect?user={login}&password={password}&host={host}&port={port}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

@login_required
def disconnect_metatrader(request):
    if request.method == 'POST':
        metatrader = Metatraders.objects.get(user=request.user)
        token = metatrader.token

        # Pastikan token tidak kosong
        if token:
            disconnect_url = f"https://mt5.mtapi.be/Disconnect?id={token}"

            try:
                response = requests.get(disconnect_url)

                if response.status_code == 200:
                    # Disconnect berhasil, hapus token dari objek Metatraders
                    metatrader.token = ''
                    metatrader.save()
                    return JsonResponse({'success': True})
                else:
                    # Permintaan Disconnect gagal
                    return JsonResponse({'success': False})

            except Exception as e:
                # Terjadi kesalahan saat melakukan permintaan Disconnect
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            # Token kosong
            return JsonResponse({'success': False, 'error': 'Token is empty'})
    
    # Jika metode bukan POST, kembalikan respons JSON gagal
    return JsonResponse({'success': False})

@login_required
def index(request):
    metatrader, created = Metatraders.objects.get_or_create(user=request.user)
    form = MetatraderForm(instance=metatrader)

    if request.method == 'POST':
        form = MetatraderForm(request.POST, instance=metatrader)
        if form.is_valid():
            form.save()
            result_connect = connect_to_mt5(metatrader.login, metatrader.password, metatrader.ip_address, metatrader.port)
            if "Error" not in result_connect:
                metatrader.token = result_connect
                metatrader.save()
            return redirect('copytrade:indexcopytrade')

    return render(request, 'copytrade/index.html', {'form': form, 'metatrader': metatrader})
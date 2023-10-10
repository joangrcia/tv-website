from django.shortcuts import render, get_object_or_404
from .models import Event
from datetime import datetime
import calendar

def event_list(request):
    # Dapatkan tanggal saat ini
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month

    # Konversi angka bulan menjadi nama bulan
    month_name = calendar.month_name[month]

    # Dapatkan semua acara pada bulan ini
    events = Event.objects.filter(date__year=year, date__month=month)

    # Buat daftar unik tanggal dari acara-acara tersebut
    event_dates = set(event.date for event in events)

    context = {
        'event_dates': event_dates,
        'events': events,
        'year': year,  # Pastikan variabel-variabel ini ada dalam konteks
        'month': month,
        'month_name':month_name,
        'day': current_date.day,
    }
    return render(request, 'event/list_event.html', context)


def event_detail_by_date(request, year, month, day, event_id):
    # Konversi tahun, bulan, dan hari menjadi integer
    year = int(year)
    month = int(month)
    day = int(day)

    # Dapatkan objek acara berdasarkan ID
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
        'year': year,
        'month': month,
        'day': day,
    }

    return render(request, 'event/event_detail_by_date.html', context)


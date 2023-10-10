from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        "judul":"ini adalah halaman calender",
    }
    return render(request, "tablesApp/index.html", context)
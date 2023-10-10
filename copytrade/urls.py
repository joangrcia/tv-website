from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'copytrade'

urlpatterns = [
    path('', views.index, name='indexcopytrade'),
    path('disconnect_metatrader/', views.disconnect_metatrader, name='disconnect_metatrader'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
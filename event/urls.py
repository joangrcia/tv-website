from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('events/<int:year>/<int:month>/<int:day>/<int:event_id>/', views.event_detail_by_date, name='event_detail_by_date'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
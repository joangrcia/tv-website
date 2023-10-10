from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('event/', include('event.urls')),
    path('profile/', include('profileApp.urls')),
    path('settings/', include('settingsApp.urls')),
    path('tables/', include('tablesApp.urls')),
    path('copytrade/', include('copytrade.urls')),
    path('videocourse/', include('video_learning.urls')),
    path('market/', include('productapp.urls')),
    path('blog/', include('articelApp.urls')),
    path('event/', include('event.urls')),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('register', views.register, name='signup'),
    path('check-email/', views.emailcheck, name='emailcheck'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dahboard/not_found', views.not_found, name='notfound'),
    path('dashboard/chart', views.index_chart, name='chart'),
    path('logout/', views.index_logout, name='indexlogout'),
    path('', views.index, name='login'),
    path('accounts/', include("allauth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'mywebsite.views.tampilan_404'
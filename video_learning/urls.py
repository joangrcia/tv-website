from django.urls import path
from . import views

app_name = 'evideo'

urlpatterns = [
    path('', views.VideoListView.as_view(), name='video_list'),
    path('upload-proof/<int:video_id>/', views.UploadProofView.as_view(), name='upload_proof'),
    path('validate-payment/<int:transaction_id>/', views.ValidatePaymentView.as_view(), name='validate_payment'),
    path('course/<slug:slugInput>/', views.VideoDetailView.as_view(), name='video_detail'),
    path('video/<slug:video_slug>/<int:season_number>/<slug:slugEpisode>/', views.EpisodeDetailView.as_view(), name='episode_detail'),
]

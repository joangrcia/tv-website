from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Episode, PaymentTransaction, Season
from .forms import PaymentTransactionForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(login_required, name='dispatch')
class VideoListView(View):
    def get(self, request):
        target_category1 = "basic"
        target_category2 = "intermediate"
        target_category3 = "master"
        videos_basic = Video.objects.filter(categories__name=target_category1)
        videos_inter = Video.objects.filter(categories__name=target_category2)
        videos_master = Video.objects.filter(categories__name=target_category3)
        videos = Video.objects.all()
        episode = Episode.objects.all()
        
        context = {
            'videos': videos,
            'episodes': episode,
            'basic': videos_basic,
            'inter': videos_inter,
            'master': videos_master,
        }
        return render(request, 'video_learning/video_list.html', context)

@method_decorator(login_required, name='dispatch')
class GetSeasonsForVideoView(View):
    def get(self, request, slugInput):
        try:
            seasons = Season.objects.filter(video__slug=slugInput)
            return seasons
        except Season.DoesNotExist:
            return None

@method_decorator(login_required, name='dispatch')
class EpisodeDetailView(View):
    def get(self, request, video_slug, season_number, slugEpisode):
        episode = get_object_or_404(Episode, season__video__slug=video_slug, season__season_number=season_number, slug=slugEpisode)
        seasons = self.get_seasons_for_video(video_slug)
        season_episodes = {}
        video = get_object_or_404(Video, slug=video_slug)

        for season in seasons:
            episodes = Episode.objects.filter(season=season)
            season_episodes[season] = episodes

        context = {
            'episode': episode,
            'season_episodes': season_episodes,
            'videos': video,
        }

        return render(request, 'video_learning/episode_detail.html', context)

    def get_seasons_for_video(self, slugInput):
        try:
            seasons = Season.objects.filter(video__slug=slugInput)
            return seasons
        except Season.DoesNotExist:
            return None

@method_decorator(login_required, name='dispatch')
class VideoDetailView(View):
    def get(self, request, slugInput):
        video = get_object_or_404(Video, slug=slugInput)
        seasons = self.get_seasons_for_video(slugInput)
        season_episodes = {}

        for season in seasons:
            episodes = Episode.objects.filter(season=season)
            season_episodes[season] = episodes

        context = {
            'videos': video,
            'season_episodes': season_episodes,
        }
        return render(request, 'video_learning/video_detail.html', context)

    def get_seasons_for_video(self, slugInput):
        try:
            seasons = Season.objects.filter(video__slug=slugInput)
            return seasons
        except Season.DoesNotExist:
            return None

@method_decorator(login_required, name='dispatch')
class UploadProofView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        form = PaymentTransactionForm()
        return render(request, 'upload_proof.html', {'form': form, 'video': video})

    def post(self, request, video_id):
        video = Video.objects.get(id=video_id)

        if request.method == 'POST':
            form = PaymentTransactionForm(request.POST, request.FILES)
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.user = request.user
                transaction.video = video
                transaction.save()
                return redirect('video_list')

@method_decorator(login_required, name='dispatch')
class ValidatePaymentView(View):
    def get(self, request, transaction_id):
        transaction = PaymentTransaction.objects.get(id=transaction_id)
        # Validasi bukti pembayaran, jika valid, set is_validated menjadi True
        # tambahkan logika validasi lainnya
        transaction.is_validated = True
        transaction.save()
        return redirect('video_list')

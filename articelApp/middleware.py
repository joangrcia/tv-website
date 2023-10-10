from .models import Viewer
from django.utils import timezone
from django.template.response import TemplateResponse
from django.http import HttpResponse  # Import HttpResponse

class ViewerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Cek apakah user sudah login dan sedang melihat halaman detail blog
        if (
            request.user.is_authenticated
            and isinstance(response, TemplateResponse)  # Menggunakan HttpResponse
            and response.status_code == 200
            and 'blog_detail' in request.resolver_match.url_name
        ):
            # Ambil blog yang sedang dilihat
            blog = response.context_data.get('blog')

            if blog:
                # Cek apakah user sudah pernah melihat blog ini
                if not Viewer.objects.filter(user=request.user, blog=blog).exists():
                    Viewer.objects.create(user=request.user, blog=blog, timestamp=timezone.now())
                    print(f"Viewer added for user: {request.user}, blog: {blog}")

        return response

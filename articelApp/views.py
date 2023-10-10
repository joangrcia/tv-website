from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, Page
from django.utils import timezone

from .models import Blog, Category
from .forms import CommentForm

def blog_list(request, category=None):
    category_param = request.GET.get('category')
    
    # Filter berdasarkan kategori jika parameter kategori ada
    if category:
        try:
            category_obj = Category.objects.get(name=category)
            blogs = Blog.objects.filter(categories=category_obj)
        except Category.DoesNotExist:
            blogs = []
    else:
        blogs = Blog.objects.all()

    blog_count = blogs.count()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Hitung rentang halaman
    total_pages = paginator.num_pages
    current_page = page_obj.number
    page_range = list(range(
        max(current_page - 2, 1),
        min(current_page + 2, total_pages) + 1
    ))

    return render(request, 'articelApp/articel_list.html', {'page_obj': page_obj, 'blog_count': blog_count, 'page_range': page_range,})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all()
    tags = blog.tag.split(', ')  # Memisahkan tag berdasarkan koma dan spasi

    # Filter artikel terbaru dalam 7 hari terakhir
    seven_days_ago = timezone.now() - timezone.timedelta(days=7)
    recent_articles = Blog.objects.filter(date__gte=seven_days_ago).exclude(slug=slug)[:4]
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            form = CommentForm()
            return redirect('blog_detail', slug=slug)  # Redirect kembali ke halaman detail blog setelah mengirim komentar
    else:
        form = CommentForm()

    return render(request, 'articelApp/articel_detail.html', {'blog': blog, 'comments': comments, 'form': form, 'recent_articles': recent_articles, 'tags': tags})

def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('articel:blog_detail', slug=slug)  # Redirect kembali ke halaman detail blog setelah mengirim komentar
    else:
        form = CommentForm()
    
    return render(request, 'articelApp/add_comment.html', {'form': form})

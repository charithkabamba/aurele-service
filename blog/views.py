from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-published_at', '-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/blog_detail.html'
    context_object_name = 'post'
from django.shortcuts import render

# Create your views here.

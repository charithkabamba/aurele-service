from django.shortcuts import render

from .models import Blog, Category
# Create your views here.



def blog(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_details.html', context)
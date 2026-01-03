from django.shortcuts import render, get_object_or_404
from .models import Project


# Project list (function-based view)
def project_list(request):
    projects = Project.objects.filter(is_published=True).order_by('-published_at', '-created_at')
    return render(request, 'pages/project.html', {'projects': projects})


# Project detail (function-based view)
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, 'pages/project_detail.html', {'project': project})


def news(request):
    return render(request, 'activite/news.html')


def blog(request):
    return render(request, 'activite/blog.html')


def project(request):
    return render(request, 'pages/project.html')


def offer(request):
    return render(request, 'activite/offer.html')


def message(request):
    return render(request, 'activite/message.html')


def newsletter(request):
    return render(request, 'activite/newsletter.html')


def ESG(request):
    return render(request, 'activite/ESG.html')



from django.shortcuts import render

from . models import CatService, Service, AboutSection, Carousel

# Create your views here.

def home(request):
    about = AboutSection.objects.all()
    Carousel_items = Carousel.objects.all()
    context = {
        'about': about,
        'Carousel_items': Carousel_items,
    }
    return render(request, 'index.html', context)

def contact(request):

    return render(request, 'pages/contact.html')

def about(request):
    about = AboutSection.objects.all()
    context = {
        'about': about,
    }
    return render(request, 'pages/about.html', context)

def blog(request):
    return render(request, 'pages/blog.html')

def service(request):
    service = Service.objects.all()
    context = {
        'service': service,
    }
    return render(request, 'pages/service.html', context)

def service_details(request, id):
    service = Service.objects.get(id=id)
    context = {
        'service': service,
    }
    return render(request, 'pages/service_details.html', context)

def project(request):
    return render(request, 'pages/project.html')

def team(request):
    return render(request, 'pages/team.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')
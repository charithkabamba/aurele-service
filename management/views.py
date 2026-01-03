from django.shortcuts import render

from . models import *

# Create your views here.
# def home(request):
#     return render(request, 'index.html')
def home(request):
    about = AboutSection.objects.all()
    carousel = Carousel.objects.all()
    context = {
        'about': about,
        'carousel': carousel,
    }
    return render(request, 'index.html', context)

def contact(request):

    return render(request, 'pages/contact.html')

def about(request):
    profile = CompanyProfile.objects.all()
    values = Value.objects.all()
    mission = Mission.objects.all()
    vision = Vision.objects.all()
    capacity = Capacity.objects.all()
    technique = Technique.objects.all()

    about = AboutSection.objects.all()
    context = {
        'profile': profile,
        'values': values,
        'mission': mission,
        'vision': vision,
        'capacity': capacity,
        'technique': technique,
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

def error_404_view(request, exception):
    return render(request, 'pages/404.html')

def gallery(request):
    return render(request, 'pages/gallery.html')
from django.shortcuts import render

# Create your views here.
from .models import Service

def home(request):
    services = Service.objects.all()
    context = {

        'services': services
    }
    return render(request, 'home.html', context)

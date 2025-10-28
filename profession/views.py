from django.shortcuts import render

# Create your views here.
def profession(request):
    return render(request, 'pages/profession.html')


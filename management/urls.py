from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('service/', service, name='service'),
    path('service/<str:id>/', service_details, name='service_details'),
    path('project/', project, name='project'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('404/', error_404_view, name='404'),
    path('gallery/', gallery, name='gallery'),
]
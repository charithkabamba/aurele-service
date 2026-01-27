from django.urls import path

from .views import *

urlpatterns = [
    path('all-news/', blog ,name='blog'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
]
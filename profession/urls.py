from django.urls import path
from .views import *

urlpatterns = [
    path('profession', profession, name='profession'),
]
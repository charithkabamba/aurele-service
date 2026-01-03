from django.urls import path
from . import views

app_name = 'activite'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('activity', views.news, name='news'),
    path('blog', views.blog, name='blog'),
    path('project', views.project, name='project'),
    path('offer', views.offer, name='offer'),
    path('message', views.message, name='message'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('esg', views.ESG, name='esg'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lounge/', views.member_lounge, name='lounge'),
    path('office/', views.manager_office, name='office'),
]
from django.contrib import admin
from django.urls import path
from . import views
from .views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name = 'home'),
    path('welcome', welcome.as_view(), name = 'welcome'),
    path('all_posts', views.all_posts, name='posts'),
]

from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.views import View

def home(request):
    return HttpResponse("Hello Blog")

class welcome(View):
    def get(self, request):
        return HttpResponse("Welcome to the Blog")



def all_posts(request):
    posts = post.objects.all()
    titles = ""
    for Post in posts:
        titles += Post.title + "<br>"

    return HttpResponse(titles)
    

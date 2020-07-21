from django.shortcuts import render
import requests
from .models import MainIndexPage
import json

# Create your views here.
def home(request):
    #  ,Dynamic Navbar ,Bug Report, dynamic links
    app = 'frontend_app'

    if MainIndexPage.objects.filter(app_name = app).exists():
        mainIndexPage = MainIndexPage.objects.filter(app_name = app)[0]
        context = {
                    "mainIndexPage":mainIndexPage,
                  }
        return render(request,"frontend/posts/index.html",context)
    
    return render(request,"frontend/posts/404.html")



def detail_post(request,slug):

    r = requests.get('http://127.0.0.1:8000/api/v1/post/detail/'+slug)
    z = r.json()

    if r.status_code == 200:
        app = 'frontend_app'
        if MainIndexPage.objects.filter(app_name = app).exists():
            mainIndexPage = MainIndexPage.objects.filter(app_name = app)[0]
            z['mainIndexPage'] = mainIndexPage
            return render(request,"frontend/posts/detail_post.html",z)
    return render(request,"frontend/posts/404.html",{'error' : z['error']})

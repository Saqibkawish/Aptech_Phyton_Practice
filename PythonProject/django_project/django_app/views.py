from django.db.models.fields import return_None
from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,  "django_project/index.html")

def About(request):
    return render(request,  "django_project/about.html")
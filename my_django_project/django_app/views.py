from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "django_app/home.html")

def contact(request):
    return render(request, "django_app/contact.html")

def about(request):
    return render(request, "django_app/about.html")

def service(request):
    return render(request, "django_app/service.html")

def feedback(request):
    return render(request, "django_app/feedback.html")
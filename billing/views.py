from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Welcome to the Django Home Page")
    return render(request, 'website/index.html', {'name': 'home'}) # using render to render the template and pass context data


def about(request):
    return render(request, 'website/about.html', {'name': 'about'}) # using render to render the template and pass context data


def contact(request):
    return HttpResponse("Welcome to the Django Contact Page")
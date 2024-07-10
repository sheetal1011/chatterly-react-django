from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hey there!, This is Home Page")


def about(request):
    return HttpResponse("Hey there!, This is About Page")

def contact(request):
    return HttpResponse("Contact US page")

def blog(request):
    return HttpResponse("This is blog page")
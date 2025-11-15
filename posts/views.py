from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render

def hello_world(request):
    return HttpResponse("Hello, World!")
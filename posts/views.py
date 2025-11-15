from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render

def posts_list(request):
    return render(request,'posts_list.html')
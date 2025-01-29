from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, World!")


def second(request):
    return HttpResponse("Hello, World! This is the second page. it wilssl work today")
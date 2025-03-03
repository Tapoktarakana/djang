from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def categories(request):
    return HttpResponse("<h1>gg wp</h1>")

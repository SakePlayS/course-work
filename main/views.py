from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>File uploader</h1>")

def v1(response):
    return HttpResponse("<h1>test 2 </h1>")

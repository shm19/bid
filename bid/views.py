from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def say_hello(request):
    return HttpResponse("hello") # type: ignore

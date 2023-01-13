from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_intro(request):
    return HttpResponse('<h1> Welcome to my web page </h1>')
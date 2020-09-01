from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    s='<h1>hello good morning</h1>'
    return HttpResponse(s)
def time(request):
    s='<h1>time is going on and on '
    return HttpResponse(s)

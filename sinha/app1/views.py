from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobs(request):
    s='<h1>Hello there are various jobs  present</h1>'
    return HttpResponse(s)

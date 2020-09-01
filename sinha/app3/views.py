from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def delhijobs(request):
    s='<h1> Hello the jobs are there in delhi</h1><hr>'
    return HttpResponse(s)

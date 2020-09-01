from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def hydjobs(request):
    s='<h1>Hello the jobes are there in hyd</h1>'
    return HttpResponse(s)

def punejobs(request):
    s='<h1>Hello the jobes are there in pune</h1>'
    return HttpResponse(s)


def mumbaijobs(request):
    s='<h1>Hello the jobes are there in mumbai</h1>'
    return HttpResponse(s)

def delhijobs(request):
    s='<h1>Hello the jobes are there in delhi</h1>'
    return HttpResponse(s)

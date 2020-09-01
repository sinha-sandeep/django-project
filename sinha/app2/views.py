from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def punejobs(request):
    s='<h1> there are various posibale jobs are there in Pune</h1>'
    return HttpResponse(s)

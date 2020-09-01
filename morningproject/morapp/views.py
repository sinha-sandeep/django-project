from django.shortcuts import render
import datetime
# Create your views here.
def mor(request):
    date=datetime.datetime.now()
    dict={'date':date}
    return render(request,'morapp/mor.html',context=dict)

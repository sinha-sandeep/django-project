from django.shortcuts import render
import datetime
# Create your views here.
def film(request):
    date=datetime.datetime.now()
    dir={'sandeep':1000,
    'rahul':50000,'X':date
    }

    return render(request,'filmapp/film.html',context=dir)

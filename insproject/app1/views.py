from django.shortcuts import render
import datetime

# Create your views here.
def ins(request):
    date=datetime.datetime.now()
    dir={'date':date}
    return render(request,'app1/ins.html',context=dir)

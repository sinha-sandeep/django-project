from django.shortcuts import render
import datetime
# Create your views here.
def ins(request):
    date=datetime.datetime.now()
    dic={'date':date,'sandeep':12230,'rahul':256000}
    return render(request,'app1/ins.html',context=dic)

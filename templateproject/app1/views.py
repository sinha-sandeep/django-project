from django.shortcuts import render
import datetime

# Create your views here.
def temppro(request):
    date=datetime.datetime.now()
    dict={'date_time':date,'sandeep':1000000}
    return render(request,'app1/wish.html',context=dict)

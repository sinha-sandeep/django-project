from django.urls import path
from urlsapp import views


urlpatterns = [


    path('hydjobs/', views.hydjobs),
    path('punejobs/', views.punejobs),
    path('mumbaijobs/', views.mumbaijobs),
    path('delhijobs/', views.delhijobs),
    ]

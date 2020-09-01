from django.urls import path
from filmapp import views

urlpatterns = [
    path('photo/', views.film),
]

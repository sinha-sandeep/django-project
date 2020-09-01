from django.urls import path
from morapp import views

urlpatterns = [
    path('morning/', views.mor),
]

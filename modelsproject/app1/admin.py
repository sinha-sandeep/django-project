from django.contrib import admin
from app1.models import Employee
class Employeeadmin(admin.ModelAdmin):
    list_display=['id','name','roll']
# Register your models here.
admin.site.register(Employee,Employeeadmin)

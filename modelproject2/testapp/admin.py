from django.contrib import admin
from testapp.models import Employee

class Employee_Admin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']



admin.site.register(Employee,Employee_Admin)

# Employee table is available to admin interface
# which data column is dispaly is totally take care by em
# Register your models here.

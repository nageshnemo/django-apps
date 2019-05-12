from django.contrib import admin
from testapp.models import Employee
# here we are importing Employee class from testapp models.property
# Register your models here.

class Employee_Admin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']

admin.site.register(Employee,Employee_Admin)
# what we are doing here is registering our Employee to admin interface
# so that we can able to see these employee table_name

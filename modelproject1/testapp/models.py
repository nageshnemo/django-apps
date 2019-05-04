from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length = 64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length = 64)

# table_name = testapp_employee
# field name = eno,ename,esal and eaddr
# behaviour
# eno is of int contenttypes
# ename is of char type and max no of allowed characters are = 64

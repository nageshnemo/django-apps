from django.db import models

# Create your models here.

class Employee(models.Model):
    # Model is a class which is present in models

    eno = models.IntegerField()
    ename = models.CharField(max_length = 64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length = 64)

    def __str__(self):
            return self.ename

# table_name = testapp_employee
# field name = eno,ename,esal and eaddr
# behaviour
# eno is of int contenttypes
# ename is of char type and max no of allowed characters are = 64
# Model is a python class which is present in models
# employee is a child class models.models

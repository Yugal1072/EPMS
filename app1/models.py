from django.db import models


# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skills = models.CharField(max_length=100, null=False)
    marital_status = models.CharField(max_length=20, null=False)
    department = models.CharField(max_length=50, null=False)
    position = models.CharField(max_length=50, null=False)


    def __str__(self):
        return self.name


class Details(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    salary = models.IntegerField()
    feedback = models.TextField()
    
    def __str__(self) -> str:
        return self.employee.name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(models.Model):
    Role_Choice = [
        ('student','student'),
        ('department','Department'),
    
]
    
    role = models.CharField(max_length=100,choices=Role_Choice,default='Student')
    year_of_study = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username
    
class Department(models.Model):
    department_name = models.CharField(max_length=200)
    description = models.TextField()
    code = models.CharField(max_length=50,unique=True)
    head_of_department = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True,related_name='department_head',limit_choices_to={'Role':'head_of_department'})

    def __str__(self):
        return self.department_name
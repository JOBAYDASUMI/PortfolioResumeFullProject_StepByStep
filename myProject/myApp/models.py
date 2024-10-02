from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    
    USER=[
        ('recruter','Recruter'),
        ('jobseeker','Jobseeker'),
    ]
    user_type=models.CharField(max_length=100,null=True,blank=True,choices=USER)
    

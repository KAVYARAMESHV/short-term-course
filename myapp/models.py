from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class course(models.Model):
    cname = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50,default="")
    qualification = models.CharField(max_length=100,default="")
    fee = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    image = models.FileField(max_length=500,default="")





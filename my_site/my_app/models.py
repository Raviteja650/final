from django.db import models

# Create your models here.


class Responseneed(models.Model):
    name=models.CharField(max_length=50)
    msg=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

class details(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

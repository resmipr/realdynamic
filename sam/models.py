from django.db import models


# Create your models here.
class Newclasses(models.Model):
    head = models.CharField(max_length=255)
    des = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')


class data(models.Model):
    heading = models.CharField(max_length=255)
    designation = models.CharField(max_length=1000)
    imges = models.ImageField(upload_to='pic')

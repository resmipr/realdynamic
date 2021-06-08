from django.db import models


class Newclass(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class Contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=1080)

from django.db import models

# Create your models here.


class register(models.Model):
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=16)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=8)





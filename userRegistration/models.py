from django.db import models

# Create your models here.
class UserReg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    
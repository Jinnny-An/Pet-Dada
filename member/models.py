from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_add = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=50)
    date_joined = models.DateTimeField()

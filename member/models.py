from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    user_phone = models.CharField(max_length=11)
    profile_img = models.FileField(upload_to='media', null=True, blank = True)
    
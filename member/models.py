from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    user_ph = models.CharField(max_length=11,default='')
    profile_img = models.FileField(upload_to='media', null=True, blank = True)
    last_name = models.CharField(max_length=200, default='')
    
    

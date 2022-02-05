from django.db import models
from django.db.models.fields import *
from member.models import User as UserAb

class Pet(models.Model):
    pet_name = CharField(max_length=50, null=True, blank=True)
    gender = CharField(max_length=1, null=True, blank=True)
    age = DateField(null=True, blank=True)
    size = CharField(max_length=1, null=True, blank=True)
    neutered = CharField(max_length=1, null=True, blank=True)
    pet_img = models.FileField(upload_to='media', null=True, blank = True)
    user = models.OneToOneField(UserAb, on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return self.pet_name



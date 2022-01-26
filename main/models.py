from django.db import models
from django.db.models.fields import *

class User(models.Model):
    user_id = AutoField(primary_key=True)
    user_name = CharField(max_length=50)
    email = CharField(max_length=100)
    user_addr = CharField(max_length=250)
    user_phone = CharField(max_length=15)
    profile_img = models.FileField(blank=True)
    pwd = CharField(max_length=50)

class Category(models.Model):
    c_id = AutoField(primary_key=True)
    c_name = CharField(max_length=50)

class Store(models.Model):
    store_id = AutoField(primary_key=True)
    store_name = CharField(max_length=50)
    store_addr = CharField(max_length=250)
    phone = CharField(max_length=20)
    time = TextField()
    store_img = models.ImageField(upload_to="static", blank = True)
    intro = TextField()
    c_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, db_column='c_id')
    created_at = DateTimeField()
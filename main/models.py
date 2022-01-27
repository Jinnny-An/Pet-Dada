from pyclbr import Class
from django.db import models
from sqlalchemy import ForeignKey

class User(models.Model):
    # PK는 기본 제공 기능 사용
    user_name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    eamil = models.CharField(max_length=100)
    user_addr = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=11)
    profile_img = models.ImageField()

    class Meta:
        db_table = 'user_main'

class Category(models.Model):
    c_name = models.CharField(max_length=50)
    
class Store(models.Model):
    # PK는 기본 제공 기능 사용
    store_name = models.CharField(max_length=50)
    store_addr = models.CharField(max_length=250)
    store_phone = models.CharField(max_length=11)
    time = models.TextField()
    # blank - 사진 업로드가 필수적이지 않음을 설정
    store_img = models.ImageField(blank=True)
    intro = models.TextField()
    # 객체가 생성되는 시간을 자동으로 저장해줌
    created_at = models.DateTimeField(auto_now_add=True)
    # 객체가 저장되는 시간을 자동으로 저장해줌
    modified_at = models.DateTimeField(auto_now=True)
    # db_column을 설정하지 않으면 c_id_id로 저장됨
    c_id = ForeignKey('Category', db_column='c_id')

    class Meta:
        db_table = 'store'




    

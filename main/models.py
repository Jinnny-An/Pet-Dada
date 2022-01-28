from asyncio.windows_events import NULL
from pyclbr import Class
from tkinter import CASCADE
from django.db import models
from sqlalchemy import ForeignKey

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=50)
#     pwd = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     user_addr = models.CharField(max_length=250)
#     user_phone = models.CharField(max_length=30)
#     profile_img = models.FileField(upload_to='%Y%m%d', null=True, blank = True)

#     class Meta:
#         db_table = 'user_main'
#         managed = False

class Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)

    class Meta:
        managed = False
    
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=50)
    store_addr = models.CharField(max_length=250)
    store_phone = models.CharField(max_length=30)
    time = models.TextField()
    # blank - 사진 업로드가 필수적이지 않음을 설정
    store_img = models.FileField(upload_to='main/static/', null=True, blank = True)
    intro = models.TextField()
    # 객체가 생성되는 시간을 자동으로 저장해줌
    created_at = models.DateTimeField(auto_now_add=True)
    # db_column을 설정하지 않으면 c_id_id로 저장됨
    c_id = models.ForeignKey('Category', db_column='c_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'store'




    

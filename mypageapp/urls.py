from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mypageapp'

urlpatterns = [
    # path('user/<int:id>/', views.update_user, name = 'update_user'),
    path('user/', views.update_user, name = 'update_user'),

    path('user/pet/', views.create_pet, name ='create_pet'),

    path('update/', views.update_pet, name='update_pet'),
    
    path('delete/', views.delete_user_img, name='delete_user_img'),


]

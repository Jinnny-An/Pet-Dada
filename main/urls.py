from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('pet_main/', views.show_main),
    path('pet_main/show/', views.show),
    
    path('req/get/', views.ajaxGet),
]
from django.urls import path
from . import views

urlpatterns = [
    path('pet_main/', views.show_main),
    path('pet_main/show/', views.show),
    path('insert/', views.insert),
    path('req/get/', views.ajaxGet),
]
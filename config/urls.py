from django.contrib import admin
from django.urls import path, include
from member import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('member/', include('member.urls')),
    path('home/', views.home),
    path('back/', views.back),
    # path('resignup/', views.resignup, name="resignup"),
    path('mypage/', include('mypageapp.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

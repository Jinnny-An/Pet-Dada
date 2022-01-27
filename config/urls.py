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
<<<<<<< HEAD
    #path('resignup/', views.resignup, name="resignup"),
    path('mypage', include('mypageapp.urls')),
=======
    # path('resignup/', views.resignup, name="resignup"),
    path('mypage/', include('mypageapp.urls')),
>>>>>>> 0f6f996096df881789e261c8ea3f4da83d7a8ea7
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

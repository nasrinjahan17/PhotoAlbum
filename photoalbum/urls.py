from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from albumapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('all/',views.home,name='all'),
    path('delete_photo/<id>/',views.delete_photo,name='delete_photo'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

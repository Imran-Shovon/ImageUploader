
from django import conf
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#from imageuploader import myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app_config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls'), name='weather'),
]

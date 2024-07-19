from django.contrib import admin
from django.urls import path, include

from app_config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls', namespace='weather')),
    path('user/', include('users.urls', namespace='user')),
]

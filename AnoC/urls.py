# AnoC/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),  # URL gốc trỏ đến ứng dụng home
]
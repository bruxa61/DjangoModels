from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicos.urls')),  # Inclui as URLs do seu aplicativo
    path('', include('accounts.urls')),  # Inclui as URLs do seu aplicativo    
]  
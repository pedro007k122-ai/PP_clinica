# CentroMedicoZenithDB/urls.py

from django.contrib import admin
from django.urls import path, include # <-- ADICIONE O 'include' AQUI

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🌟 ADICIONE ESTA LINHA 🌟
    # Inclui todas as rotas definidas no seu app 'data_base'
    path('', include('data_base.urls')), 
]
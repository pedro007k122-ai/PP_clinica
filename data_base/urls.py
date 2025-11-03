from django.urls import path
from . import views

urlpatterns = [
    # URL Raiz (Home)
    path('', views.home, name='home'),

    # --- URLs de FISIOTERAPIA ---
    path(
        'fisioterapia/cadastrar/', 
        views.cadastrar_agendamento_fisioterapia, 
        name='cadastrar_agendamento_fisioterapia'
    ),
    path(
        'fisioterapia/listar/', 
        views.listar_agendamentos_fisioterapia, 
        name='listar_agendamentos_fisioterapia'
    ),

    # --- NOVAS URLs de PSICOLOGIA ---
    path(
        'psicologia/cadastrar/', 
        views.cadastrar_agendamento_psicologia, 
        name='cadastrar_agendamento_psicologia'
    ),
    path(
        'psicologia/listar/', 
        views.listar_agendamentos_psicologia, 
        name='listar_agendamentos_psicologia'
    ),
]
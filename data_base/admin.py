from django.contrib import admin
from .models import agendamentos_fisioterapia, agendamentos_psicologia

@admin.register(agendamentos_fisioterapia)
class Adminagendamentos_fisioterapiaadmin(admin.ModelAdmin):
    pass 



@admin.register(agendamentos_psicologia)
class Adminagendamentos_psicologiaadmin(admin.ModelAdmin):
    pass

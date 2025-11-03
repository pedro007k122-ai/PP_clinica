from django.db import models
from django.contrib.auth.models import User

class agendamentos_fisioterapia(models.Model):
    Cliente = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False)
    idade = models.IntegerField(blank=False)
    sexo = models.CharField(max_length=30, blank=False)
    telefone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    data_e_hora = models.DateTimeField(blank=False)
    tipo_de_consulta = models.CharField(max_length=20, blank=False)
    #Preferência de sexo do proffisional que deve prestar atendimento ao cliente.
    pdsp = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.nome
    


class agendamentos_psicologia(models.Model):
    Cliente = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False)
    idade = models.IntegerField(blank=False)
    sexo = models.CharField(max_length=30, blank=False)
    telefone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    data_e_hora = models.DateTimeField(blank=False)
    tipo_de_consulta = models.CharField(max_length=20, blank=False)
    #Preferência de sexo do proffisional que deve prestar atendimento ao cliente.
    pdsp = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.nome
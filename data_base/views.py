from django.shortcuts import render, redirect
from django.http import HttpResponse
# Importa os dois modelos
from .models import agendamentos_fisioterapia, agendamentos_psicologia 

# --- Funções de Agendamento de FISIOTERAPIA ---

def cadastrar_agendamento_fisioterapia(request): # Função renomeada para ser específica
    # Verifica se a requisição é um POST (envio de formulário)
    if request.method == 'POST':
        # 1. Coleta os dados do formulário (POST)
        cliente = request.POST.get('cliente')
        cpf = request.POST.get('cpf')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        data_e_hora = request.POST.get('data_e_hora')
        tipo_de_consulta = request.POST.get('tipo_de_consulta')
        pdsp = request.POST.get('pdsp') # Preferência de sexo do profissional

        # 2. Cria uma nova instância do modelo de FISIOTERAPIA
        try:
            agendamentos_fisioterapia.objects.create(
                Cliente=cliente,
                cpf=cpf,
                idade=int(idade) if idade else 0, 
                sexo=sexo,
                telefone=telefone,
                email=email,
                data_e_hora=data_e_hora,
                tipo_de_consulta=tipo_de_consulta,
                pdsp=pdsp
            )
            return HttpResponse(f'Agendamento de FISIOTERAPIA para {cliente} realizado com sucesso!')

        except Exception as e:
            return HttpResponse(f'Erro ao cadastrar agendamento de Fisioterapia: {e}', status=400)

    # Se a requisição for GET, renderiza o template (que precisa ser renomeado)
    return render(request, 'cadastro/cadastrar_agendamento_fisioterapia.html')


def listar_agendamentos_fisioterapia(request): # Função renomeada para ser específica
    agendamentos = agendamentos_fisioterapia.objects.all() 
    return render(request, 'cadastro/listar_agendamentos_fisioterapia.html',
                   {'agendamentos': agendamentos})

# -----------------------------------------------

# --- NOVAS Funções de Agendamento de PSICOLOGIA ---

def cadastrar_agendamento_psicologia(request):
    # Verifica se a requisição é um POST (envio de formulário)
    if request.method == 'POST':
        # Os campos são os mesmos, então a coleta de dados se repete
        cliente = request.POST.get('cliente')
        cpf = request.POST.get('cpf')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        data_e_hora = request.POST.get('data_e_hora')
        tipo_de_consulta = request.POST.get('tipo_de_consulta')
        pdsp = request.POST.get('pdsp')

        # 2. Cria uma nova instância do modelo de PSICOLOGIA
        try:
            agendamentos_psicologia.objects.create( # <--- Usa o novo modelo aqui
                Cliente=cliente,
                cpf=cpf,
                idade=int(idade) if idade else 0, 
                sexo=sexo,
                telefone=telefone,
                email=email,
                data_e_hora=data_e_hora,
                tipo_de_consulta=tipo_de_consulta,
                pdsp=pdsp
            )
            return HttpResponse(f'Agendamento de PSICOLOGIA para {cliente} realizado com sucesso!')

        except Exception as e:
            return HttpResponse(f'Erro ao cadastrar agendamento de Psicologia: {e}', status=400)

    # Renderiza o novo template de cadastro
    return render(request, 'cadastro/cadastrar_agendamento_psicologia.html')


def listar_agendamentos_psicologia(request):
    agendamentos = agendamentos_psicologia.objects.all() # <--- Consulta o novo modelo aqui
    return render(request, 'cadastro/listar_agendamentos_psicologia.html',
                   {'agendamentos': agendamentos})

# -----------------------------------------------

# --- Função Home Original ---
def home (request):
    return HttpResponse('TESTE')
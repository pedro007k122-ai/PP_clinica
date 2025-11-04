# PP-Clínica: Sistema de Gerenciamento Médico

Este projeto é uma aplicação web completa desenvolvida em Django para gerenciar o cadastro de pacientes, agendamentos e informações médicas para a clínica fictícia **Centro Médico Zenith **.

O sistema foi estruturado para ser intuitivo e eficiente.

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Web:** Django (Versão baseada no `requirements.txt`)
* **Banco de Dados:** SQLite (Padrão de desenvolvimento)
* **Front-end:** HTML, CSS (com estrutura de template do Django)
* **Controle de Versão:** Git e GitHub

---

## 🚀 Passo a Passo para Execução (Setup)

Siga estas instruções para clonar e rodar o projeto em um ambiente local:

### 1. Requisitos

Certifique-se de ter o **Python (versão 3.8 ou superior)** e o **Git** instalados na sua máquina.

### 2. Clonagem do Repositório

Abra o seu terminal (ou Git Bash) e execute:

```bash
git clone [https://github.com/pedro007k122-ai/PP_clinica.git](https://github.com/pedro007k122-ai/PP_clinica.git)
cd PP_clinica
3. Configuração do Ambiente Virtual
É essencial rodar o projeto em um ambiente virtual (venv) limpo:

Bash

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Exemplo para Windows/Git Bash)
source venv/Scripts/activate

# Para Linux/macOS, use:
# source venv/bin/activate
4. Instalação das Dependências
Com o ambiente virtual ativo, instale todas as bibliotecas listadas no arquivo requirements.txt:

Bash

pip install -r requirements.txt
5. Configuração do Banco de Dados
Aplique as migrações para criar as tabelas no banco de dados SQLite:

Bash

python manage.py migrate
6. Criação de Superusuário (Opcional)
Se desejar acessar o painel de administração do Django:

Bash

python manage.py createsuperuser
Siga as instruções para criar login e senha.

7. Iniciar o Servidor
Inicie o servidor de desenvolvimento do Django:

Bash

python manage.py runserver
🌐 Acesso ao Sistema
O sistema estará rodando localmente. Você pode acessá-lo no seu navegador através do seguinte endereço:

http://127.0.0.1:8000/

O painel de administração (se você criou o superusuário) pode ser acessado em:

http://127.0.0.1:8000/admin/


### Último Passo

Depois de salvar o arquivo como `README.md` na raiz do seu projeto, use o Terminal para enviá-lo ao GitHub:

```bash
git add README.md
git commit -m "Adiciona README.md com documentação e instruções de setup"
git push
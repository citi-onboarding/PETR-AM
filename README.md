# PETR-AM
Repositório do site da PETR-AM Jr.

Necessário ter python na máquina. Caso não tenha:

Windows - https://www.python.org/downloads/ Linux - sudo apt install python3.7

Confira se o Python foi instalado digitando python

Instalando Django:
pip install django

Criando um ambiente virtual:

Criar a pasta do projeto

mkdir sua_pasta

Entrem na pasta:

cd sua_pasta

dentro da pasta do projeto, rode o comando:

python -m venv env

Ativando o ambiente virtual:
env\Scripts\activate

Criando um projeto em Django
Na pasta do projeto (fora da pasta do ambiente virtual), rode o comando:

django-admin startproject nome_do_seu_projeto

cd nome_do_seu_projeto

criando um app

python manage.py startapp nome_do_seu_app

abrir o arquivo settings.py e em INSTALLED_APPS adicionar 'nome_do_seu_app'

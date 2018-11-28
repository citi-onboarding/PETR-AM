# PETR-AM
Repositório do site da PETR-AM Jr.

Necessário ter python na máquina. Caso não tenha:

Windows - https://www.python.org/downloads/ Linux - sudo apt install python3.7

Confira se o Python foi instalado digitando python e verifique a versão om python -V

Dentro da pasta do projeto, rode o comando:
  python -m venv env

Ativando o ambiente virtual:
  Windows
    env\Scripts\activate
  Linux
    source env/bin/activate

Instalando Django:
  pip install django

Se necessário de update no pip:
  python -m pip install --upgrade pip

Verifique se os requerimentos batem com os atuais usando:
  pip freeze

Para rodar, na pasta onde há o manage.py use:
  python manage.py runserver
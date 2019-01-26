from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Servico, Funcionario
from django.core.mail import send_mail
def home_view(request):
    if request.method == 'POST':
        send_mail(
            '[CONTATO-SITE] - [{}]'.format(request.POST.get('assunto')),
            'Nome: {}\nEmail: {}\nTelefone: {}\nComo nos conheceu: {}\nMensagem: {}'.format(
                request.POST.get('nome'),
                request.POST.get('email'),
                request.POST.get('phone'),
                request.POST.get('conheceu'),
                request.POST.get('mensagem')
            ),
            'petrambot@gmail.com',
            ['petrambot@gmail.com'],#todos os emails destinatários(colocar o email aki)
            fail_silently = False,
        )
    context = get_context()
    return render(request, "home.html", context)

def get_context():
    return {
        'servicos': Servico.objects.all().order_by('-titulo'),
        'funcionarios': Funcionario.objects.all().order_by('-nome')
    }

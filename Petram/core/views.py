from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Servico, Funcionario
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from templated_email import send_templated_mail


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all().order_by('-titulo')
        context["funcionarios"] = Funcionario.objects.all().order_by('-nome')
        return context

def ContactView(request):
    if request.method == 'POST':#se tentarmos dar post no form
        name = request.POST.get('nome')#pegamos o nome
        email = request.POST.get('email')#pegamos o email
        phone = request.POST.get('phone')#pegamos o numero
        conheceu = request.POST.get('conheceu')#pegamos o como conheceu
        mensagem = request.POST.get('mensagem')#pegando a mensagem
        assunto = request.POST.get('assunto')#pegando o assunto
        send_templated_mail(
            template_name='email',
            from_email='email',
            recipient_list=['PetramContatoBot@outlook.com'],#todos os emails destinatários
            context={
                'assunto: ': assunto,
                'nome: ': name,
                'email: ': email,
                'telefone para contato: ': phone,
                'mensagem: ': mensagem,
                'como nos conheceu: ': conheceu
            }
        )
        return HttpResponseRedirect(reverse_lazy('home'))
    return(render(request, 'home.html'))
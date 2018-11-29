from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Servico
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all().order_by('-titulo')
        return context

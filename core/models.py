from django.db import models
#classe das screens do carrossel de serviços

class Servico(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='servicos/', null=False, blank=False)

    class Meta: 
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços' #avisa ao django que tem o plural

    def __str__(self):
        return self.titulo

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to='equipe/', null=False, blank=False)
    função = models.CharField(max_length=100, null=False, blank=False)
    descrição = models.TextField(null=False, blank=False)

    class Meta: 
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários' #avisa ao django que tem o plural

    def __str__(self):
        return self.nome
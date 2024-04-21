from django.db import models
from django.urls import reverse


# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return f'{self.nome} [{self.email}]'
    
    class Meta:
      verbose_name = 'Formulário de cadastro'
      verbose_name_plural = 'Formulário de cadastro'
      ordering = ['-data']

def clean_password(self):
        senha = self.cleaned_data['senha']
        return make_password(senha)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('detalhes_produto', args=[str(self.pk)])


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'



      

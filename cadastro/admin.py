from django.contrib import admin
from cadastro.models import Cadastro
from .models import Produto


# Register your models here.
@admin.register(Cadastro)

class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco']
    search_fields = ['nome', 'descricao']
    list_filter = ['preco']
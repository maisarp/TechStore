from django.shortcuts import render
from django.http import HttpResponse
from cadastro.forms import CadastroForm
from cadastro.models import Cadastro
from cadastro.models import Produto  
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.shortcuts import redirect


# Create your views here.

class InicioView(ListView):
    model = Produto
    template_name = 'inicio.html'
    context_object_name = 'produtos'

def inicio(request):
    produtos = Produto.objects.all()  
    contexto = {
        'produtos': produtos
    }
    return render(request, 'inicio.html', contexto)

def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def cpu_gamer(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    return render(request, 'cpu.html', {'produto': produto})

def cadastro(request):
    sucesso = False
    mensagem = None

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Cadastro.objects.filter(email=email).exists():
                mensagem = "E-mail já cadastrado!"
            else:
                form.save()
                sucesso = True
                mensagem = "Cadastro realizado com sucesso!"
    else:
        form = CadastroForm()

    contexto = {
        'form': form,
        'sucesso': sucesso,
        'mensagem': mensagem
    }
    return render(request, 'cadastro.html', contexto)

def pesquisar(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Produto.objects.filter(nome__icontains=query)

    return render(request, 'pesquisa.html', {'query': query, 'resultados': resultados})
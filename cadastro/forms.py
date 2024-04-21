from django import forms
from cadastro.models import Cadastro
from django.contrib.auth.hashers import make_password
from .models import Produto


class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),  
        }

    def save(self, commit=True):
        cadastro = super(CadastroForm, self).save(commit=False)
        senha = self.cleaned_data["senha"]  
        cadastro.senha = make_password(senha)
        if commit:
            cadastro.save()  
        return cadastro

from django import forms
from .models import Fornecedor, Categoria, Produto


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_fantasia', 'email', 'telefone']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def clean_preco(self):
        preco = self.cleaned_data['preco']
        if float(preco) < 0:
            raise forms.ValidationError('Preço inválido')
        return preco

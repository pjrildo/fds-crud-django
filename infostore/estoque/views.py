from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Fornecedor, Categoria, Produto
from .forms import FornecedorForm, CategoriaForm, ProdutoForm


def buscar_produtos_categoria(request, pk):
    produtos = Produto.objects.filter(categoria_id=pk).select_related()
    return render(request, 'produto/buscar.html', {'produtos_categoria': produtos})


def buscar_produtos_fornecedor(request, pk):
    produtos = Produto.objects.filter(fornecedor_id=pk).select_related()
    return render(request, 'produto/buscar.html', {'produtos_fornecedor': produtos})


def confirma_fornecedor_delete(request, pk):
    fornecedor = Fornecedor.objects.filter(id=pk).first()
    return render(request, 'fornecedor/delete.html', {'fornecedor': fornecedor})


def confirma_categoria_delete(request, pk):
    categoria = Categoria.objects.filter(id=pk).first()
    return render(request, 'categoria/delete.html', {'categoria': categoria})


def confirma_produto_delete(request, pk):
    produto = Produto.objects.filter(id=pk).first()
    return render(request, 'produto/delete.html', {'produto': produto})


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor/listar.html'
    context_object_name = 'fornecedores'


class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'fornecedor/criar.html'
    form_class = FornecedorForm
    success_url = reverse_lazy('fornecedores_fornecedor_list')


class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = ['email', 'telefone']
    template_name = 'fornecedor/atualizar.html'
    success_url = reverse_lazy('fornecedores_fornecedor_list')


class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'fornecedor/delete.html'
    context_object_name = 'fornecedor'
    success_url = reverse_lazy('fornecedores_fornecedor_list')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'
    context_object_name = 'categorias'


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria/criar.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias_categoria_list')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'categoria/atualizar.html'
    success_url = reverse_lazy('categorias_categoria_list')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/delete.html'
    context_object_name = 'categoria'
    success_url = reverse_lazy('categorias_categoria_list')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listar.html'
    context_object_name = 'produtos'


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto/criar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('produtos_produto_list')


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = '__all__'
    template_name = 'produto/atualizar.html'
    success_url = reverse_lazy('produtos_produto_list')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/delete.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('produtos_produto_list')




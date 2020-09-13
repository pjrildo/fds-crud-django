from django.urls import path
from .views import FornecedorListView, FornecedorCreateView, \
    FornecedorDeleteView, FornecedorUpdateView, CategoriaListView, \
    CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, \
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    buscar_produtos_categoria, buscar_produtos_fornecedor

urlpatterns = [
    path('fornecedores/', FornecedorListView.as_view(), name='fornecedores_fornecedor_list'),
    path('fornecedores/criar', FornecedorCreateView.as_view(), name='fornecedores_fornecedor_create'),
    path('fornecedores/<int:pk>/delete', FornecedorDeleteView.as_view(), name='fornecedores_fornecedor_delete'),
    path('fornecedores/<int:pk>/update', FornecedorUpdateView.as_view(), name='fornecedores_fornecedor_update'),
    path('categorias/', CategoriaListView.as_view(), name='categorias_categoria_list'),
    path('categorias/criar', CategoriaCreateView.as_view(), name='categorias_categoria_create'),
    path('categorias/<int:pk>/delete', CategoriaDeleteView.as_view(), name='categorias_categoria_delete'),
    path('categorias/<int:pk>/update', CategoriaUpdateView.as_view(), name='categorias_categoria_update'),
    path('produtos/', ProdutoListView.as_view(), name='produtos_produto_list'),
    path('produtos/criar', ProdutoCreateView.as_view(), name='produtos_produto_create'),
    path('produtos/<int:pk>/update', ProdutoUpdateView.as_view(), name='produtos_produto_update'),
    path('produtos/<int:pk>/delete', ProdutoDeleteView.as_view(), name='produtos_produto_delete'),
    path('produtos/buscar/categoria/<int:pk>', buscar_produtos_categoria),
    path('produtos/buscar/fornecedor/<int:pk>', buscar_produtos_fornecedor),
]

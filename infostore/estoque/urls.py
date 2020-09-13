from django.urls import path
from .views import FornecedorListView, FornecedorCreateView, \
    FornecedorDeleteView, FornecedorUpdateView, CategoriaListView, \
    CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, \
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    buscar_produtos_categoria, buscar_produtos_fornecedor, confirma_fornecedor_delete, \
    confirma_categoria_delete, confirma_produto_delete

urlpatterns = [
    path('fornecedores/', FornecedorListView.as_view(), name='fornecedores_fornecedor_list'),
    path('fornecedores/criar', FornecedorCreateView.as_view(), name='fornecedores_fornecedor_create'),
    path('fornecedores/delete/<int:pk>', FornecedorDeleteView.as_view(), name='fornecedores_fornecedor_delete'),
    path('fornecedores/confirma/<int:pk>', confirma_fornecedor_delete, name='fornecedores_confirma_delete'),
    path('fornecedores/update/<int:pk>', FornecedorUpdateView.as_view(), name='fornecedores_fornecedor_update'),
    path('categorias/', CategoriaListView.as_view(), name='categorias_categoria_list'),
    path('categorias/criar', CategoriaCreateView.as_view(), name='categorias_categoria_create'),
    path('categorias/delete/<int:pk>', CategoriaDeleteView.as_view(), name='categorias_categoria_delete'),
    path('categorias/confirma/<int:pk>', confirma_categoria_delete, name='categorias_confirma_delete'),
    path('categorias/update/<int:pk>', CategoriaUpdateView.as_view(), name='categorias_categoria_update'),
    path('produtos/', ProdutoListView.as_view(), name='produtos_produto_list'),
    path('produtos/criar', ProdutoCreateView.as_view(), name='produtos_produto_create'),
    path('produtos/update/<int:pk>', ProdutoUpdateView.as_view(), name='produtos_produto_update'),
    path('produtos/delete/<int:pk>', ProdutoDeleteView.as_view(), name='produtos_produto_delete'),
    path('produtos/confirma/<int:pk>', confirma_produto_delete, name='produtos_confirma_delete'),
    path('produtos/buscar/categoria/<int:pk>', buscar_produtos_categoria, name="buscar_produtos_categoria"),
    path('produtos/buscar/fornecedor/<int:pk>', buscar_produtos_fornecedor),
]

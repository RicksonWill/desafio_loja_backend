from rest_framework import viewsets
from loja.models import Produto
from loja.serializer import ProdutoSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerializer


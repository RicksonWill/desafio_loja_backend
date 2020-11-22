from rest_framework import serializers
from loja.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Produto
    fields = ['id','name','cod','value','qtd']
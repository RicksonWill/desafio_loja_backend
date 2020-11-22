from django.contrib import admin
from loja.models import Produto


class Produtos(admin.ModelAdmin):
  list_display = ('id','name','cod','value','qtd')
  list_display_links = ('id','name')
  search_fields = ('name',)

admin.site.register(Produto, Produtos)
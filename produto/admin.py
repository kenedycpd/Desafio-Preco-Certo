from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAmin(admin.ModelAdmin):
	list_display = ('nome', 'preco_custo', 'preco_venda')
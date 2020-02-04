from django.db import models

# Modelo Produto.
class Produto(models.Model):
	nome = models.CharField('Descrição', max_length=100)
	preco_custo = models.DecimalField('Preço Custo', max_digits=7, decimal_places=2)
	preco_venda = models.DecimalField('Preço Venda', max_digits=7, decimal_places=2)
	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
	def __str__(self):
		return self.nome
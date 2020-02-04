
from django.db import models
from clinte.models import Cliente
from produto.models import Produto

# Modelo Pedido.
class Pedido(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
	quantidade = models.IntegerField('Quantidade')
	data = models.DateField('Criado em', auto_now_add=True)

	def calcula(self):
		return self.preco / self.quantidade
	preco_medio = property(calcula)

	def total(self):
		return self.preco * self.quantidade
	sub_total = property(total)


	class Meta:
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'
		ordering = ['cliente']
	def __str__(self):
		return "%s" % self.produto
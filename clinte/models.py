from django.db import models

# Modelo Cliente.
class Cliente(models.Model):
	nome = models.CharField('Nome', max_length=50)
	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
	def __str__(self):
		return self.nome
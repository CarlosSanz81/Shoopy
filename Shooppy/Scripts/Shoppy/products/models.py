from django.db import models
from clientes.models import Cliente
class Product(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)
	categoria = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.nombre


	class Meta:
		ordering = ('-precio',)

class Favorito(models.Model):
	user = models.ForeignKey(Cliente)
	product = models.ForeignKey(Product)

	class Meta:
		verbose_name = 'Favorito'
		verbose_name_plural = 'Favoritos'

	def __str(self):
		return '%s  %s' % (self.user.name, self.product.name)
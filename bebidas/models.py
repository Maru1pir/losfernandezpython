from django.db import models

# Create your models here.

#lo cambiaria por pais de origen o algo asi
class Distribuidor(models.Model):
	nombre = models.CharField(max_length=40)
	rut = models.IntegerField()
	direccion = models.CharField(max_length=40)
	sitioweb = models.URLField(blank=True)
	email = models.EmailField(blank=True)
	foto = models.ImageField(upload_to='imagenes')

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Distribuidores'

class Bebidas(models.Model):
	descripcion = models.CharField(max_length=50)
	precio = models.CharField(max_length=15)
	origen = models.CharField(max_length=40)
	stock = models.IntegerField(blank=True, null=True)
	distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='imagenes')
	whisky = 'wh'
	cerveza = 'ce'
	vino = 'vi'
	licor = 'li'
	tipo_sel = [
		(whisky, 'whisky'),
		(cerveza, 'cerveza'),
		(vino, 'vino'),
		(licor, 'licor')
	]
	tipo = models.CharField(
		max_length=2,
		choices=tipo_sel,
		default=vino
		)

	def __str__(self):
		return '%s %s' % (self.tipo, self.origen)

	class Meta:
		verbose_name_plural = 'Bebidas'
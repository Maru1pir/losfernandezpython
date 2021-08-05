from django.contrib import admin
from bebidas.models import Distribuidor, Bebidas

# Register your models here.

class DistribuidorAdmin(admin.ModelAdmin):
	search_fields = ('nombre', 'direccion')
	list_display = ('nombre', 'direccion', 'email')
	ordering = ('nombre',)

class BebidasAdmin(admin.ModelAdmin):
	search_fields = ('tipo', 'descripcion')
	list_display = ('descripcion', 'origen', 'tipo', 'precio', 'stock')
	ordering = ('descripcion', 'origen',)
	
		

admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Bebidas, BebidasAdmin)  
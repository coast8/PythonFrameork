from django.contrib import admin

# Register your models here.

from .models import Carro, Fabricante


class FabricanteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'pais')

admin.site.register(Fabricante, FabricanteAdmin)


class CarroAdmin(admin.ModelAdmin):
	list_display = ('nome', 'fabricante')

admin.site.register(Carro, CarroAdmin)
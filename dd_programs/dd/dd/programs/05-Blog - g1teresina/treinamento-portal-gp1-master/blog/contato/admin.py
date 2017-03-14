from django.contrib import admin

from .models import Contato

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Contato, ContatoAdmin)
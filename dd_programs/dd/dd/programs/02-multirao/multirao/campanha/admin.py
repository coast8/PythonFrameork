from django.contrib import admin

from .models import Campanha

# Register your models here.

class CampanhaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Campanha, CampanhaAdmin)
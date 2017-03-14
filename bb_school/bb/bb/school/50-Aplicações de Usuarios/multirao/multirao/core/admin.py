from django.contrib import admin

from .models import UserProfile, Sobre, ComoFunciona

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	pass

class SobreAdmin(admin.ModelAdmin):
	list_display = ("titulo", "descricao")

class ComoFuncionaAdmin(admin.ModelAdmin):
	list_display = ("titulo", "descricao")

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Sobre, SobreAdmin)
admin.site.register(ComoFunciona, ComoFuncionaAdmin)
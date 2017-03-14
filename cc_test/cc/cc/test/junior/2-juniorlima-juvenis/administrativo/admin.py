# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from yawdadmin import admin_site
from models import Empresa, Colaboradores

class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':('nome', 'cnpj', ('website'))}),
        ('Logradouro', {'fields':('endereco',('bairro', 'cep'), ('cidade_uf',))}),
        ('Responsável para contato', {'fields':(('telefone', 'email'), ('responsavel', 'telefoneresponsavel'),)}),
        ('Extras', {'fields':['logo']}),
    ]
    list_display = ['nome', 'responsavel', 'telefone', 'website']
    search_fields = ['nome']
    save_on_top = True
    ordering = ['nome']

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Colaboradores
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
#admin_site.unregister(User)
admin_site.register(User, UserAdmin)
admin_site.register(Colaboradores)

admin_site.register(Empresa)


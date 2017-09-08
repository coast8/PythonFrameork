from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin): #classe criado para ser usada

	#vai mostrar no display
    list_display = ['name', 'slug', 'start_date', 'created_at']
    
    #para pesquisar as como parametro as variaveis passadas
    search_fields = ['name', 'slug']
    
    #para usar escrita automática com dicionários,
    #empragado em url's
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
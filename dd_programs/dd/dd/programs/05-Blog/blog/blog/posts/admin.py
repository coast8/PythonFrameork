from django.contrib import admin

from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'descricao_curta', 'data_post')


admin.site.register(Post, PostAdmin)
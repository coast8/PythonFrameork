# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.contrib import admin
from django.shortcuts import get_object_or_404

from galeria.models import Galeria, Image

from multiupload.admin import MultiUploadAdmin

class ImageInlineAdmin(admin.TabularInline):
    model = Image


class GaleriaMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, galeria, request):
        if galeria:
            image = galeria.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, galeria=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }

class GaleriaAdmin(GaleriaMultiuploadMixing, MultiUploadAdmin):
    inlines = [ImageInlineAdmin,]
    multiupload_form = True
    multiupload_list = False
    fieldsets = (
        ('Publicação', {'fields': (('publicar', 'destaque'), 'titulo', 'subtitulo', 'conteudo',)}),
        ('Classificação', {'fields': (('imagem'),)}),
    )
    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()


class ImageAdmin(GaleriaMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True


admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Image, ImageAdmin)
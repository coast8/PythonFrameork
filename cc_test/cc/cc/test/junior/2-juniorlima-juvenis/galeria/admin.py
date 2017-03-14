# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404

__author__ = 'Junior Lima'

from django.contrib import admin
from yawdadmin import admin_site
from models import Galeria, FotoGaleria

from lib.multiupload.admin import MultiUploadAdmin
from lib.sorl.thumbnail.admin import AdminImageMixin


def make_published(modeladmin, request, queryset):
    queryset.update(publicar='p')
make_published.short_description = "Mark selected stories as published"

class ImagemInlineAdmin(admin.TabularInline):
    model = FotoGaleria
    extra = 5

class ImagemAdmin(AdminImageMixin, MultiUploadAdmin):
    list_display = ('imagemAdmin', 'cliques', 'nome', 'galeria')
    list_editable = ('galeria',)
    list_filter = ('galeria',)

    # default value of all parameters:
    change_form_template = 'multiupload/change_form.html'
    change_list_template = 'multiupload/change_list.html'
    multiupload_template = 'multiupload/upload.html'
    # if true, enable multiupload on list screen
    # generaly used when the model is the uploaded element
    multiupload_list = True
    # if true enable multiupload on edit screen
    # generaly used when the model is a container for uploaded files
    # eg: gallery
    # can upload files direct inside a gallery.
    multiupload_form = True
    # max allowed filesize for uploads in bytes
    # 3 Mb
    multiupload_maxfilesize = 3 * 2 ** 20
    # min allowed filesize for uploads in bytes
    multiupload_minfilesize = 0
    # tuple with mimetype accepted
    multiupload_acceptedformats = (
        "image/jpeg",
        "image/pjpeg",
        "image/png",
    )

    def process_uploaded_file(self, uploaded, object, request):

        # example:
        galeria_id = request.POST.get('galeria_id', [''])
        title = request.POST.get('title', '') or uploaded.name
        clique = 0
        f = FotoGaleria(nome=title, img=uploaded, galeria_id=galeria_id, cliques=clique)

        f.save()
        return {
            'url': f.imagem(),
            'thumbnail_url': f.imagem(),
            'id': f.id,
            'name': f.galeria.titulo,
        }

    def delete_file(self, pk, request):
        '''
        Function to delete a file.
        '''
        # This is the default implementation.
        obj = get_object_or_404(self.queryset(request), pk=pk)
        obj.delete()

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        if db_field.name == 'galeria':
            kwargs['queryset'] = Galeria.objects.all()
        else:
            pass

        return super(ImagemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def imagem_galeria(self, obj):
        if obj.img:
            return u'<img width="170px" src=/media/%s>' % (obj.img)
        else:
            return u'<img src=/media/img/avatar.png>'

    imagem_galeria.short_description = 'Imagem'
    imagem_galeria.allow_tags = True

class GaleriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principais', {'fields':(('publicar','destaque'),('titulo'),'subtitulo','chamada')}),
        ('Conteudo', {'fields':('conteudo','imagem',)}),
    ]

    list_display = ('titulo', 'get_actions', 'criado_em', 'publicar', 'destaque')
    list_filter = ('publicar', 'destaque')
    search_fields = ('titulo',)
    inlines = [ImagemInlineAdmin]
    save_on_top= True
    actions = [make_published]

    def get_actions(self, obj):
        try:
            return u'<div align="center"><a class="btn btn-success" href="/admin/galeria/fotogaleria/multiupload/?galeria_id=%s">Adicionar Imagens</a>  <a class="btn btn-info" href="/admin/galeria/fotogaleria/?q=&galeria__noticia_ptr__exact=%s&o=-2&q=">Ver Imagens</a></div>' % (obj.id, obj.id)
        except:
            return
    get_actions.short_description = 'Ações'
    get_actions.allow_tags = True

admin_site.register(FotoGaleria, ImagemAdmin)
admin_site.register(Galeria, GaleriaAdmin)
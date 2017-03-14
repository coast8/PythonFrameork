# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from datetime import datetime
from django.contrib import admin

from design.actions import publicar_site, despublicar_site, destaque_site, del_destaque_site
from design.models import Cliente, Portifolio, Pagamento, Tipo

from adminsortable2.admin import SortableAdminMixin

def is_expired(self):
    """ Check if an invoice is expired """
    now = datetime.now().date()
    extra = ""
    image = 'img/admin/icon_success.gif'
    days_left = (self.prazo_pagamento - now).days
    if self.pago == 1: image = '/admin/img/icon_changelink.gif'
    elif self.pago == 0:
        if days_left <= 0:
            image = '/admin/img/icon_error.gif'
            extra = _(' <strong>(%s dias atrasados.)</strong>' % (days_left * -1))
        else:
            image = '/admin/img/icon_clock.gif'
            extra = _(" (%s dias restantes.)" % days_left)
    return '<img src="%(admin_media)s%(image)s" />%(extra)s' % {'admin_media': '/static',
                                                               'image': image,
                                                               'extra': extra,}

class ClienteAdmin(admin.ModelAdmin):
    class Media:
        js = (
              "/static/extra-admin/js/nonodig.js",
        )
    list_display = ('nome', 'tel_pri', 'tel_adc', 'email')

class PagamentoInline(admin.StackedInline):
    model = Pagamento
    fieldsets = [
        ('Entrega', {'fields': (('pago', 'tipo_recebimento', 'data_entrega'),)}),
        ('Pagamento', {'fields': (('prazo_pagamento', 'valor'), 'data_pagamento')}),
    ]
    extra = 0

class PortifolioAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'cliente', 'publicar', 'destaque')
    inlines = (PagamentoInline,)
    save_on_top = True
    actions = (publicar_site, despublicar_site, destaque_site, del_destaque_site)
    list_filter = ('publicar', 'destaque')
    ordering = ('-my_order',)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'portifolio', 'data_entrega', 'prazo_pagamento', 'valor', 'tipo_recebimento', is_expired)

class TipoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Portifolio, PortifolioAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Tipo, TipoAdmin)
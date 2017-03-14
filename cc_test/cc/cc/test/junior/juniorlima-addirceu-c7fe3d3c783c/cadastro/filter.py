# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class AniversarianteMesFilter(admin.SimpleListFilter):

    title = _('Aniversariante')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'data_nascimento'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('mes_atual', _('Mes atual')),
            ('mes_prox', _('Proximo mes')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        today = date.today()
        if self.value() == 'mes_atual':
            return queryset.filter(data_nascimento__month=today.month)
        if self.value() == 'mes_prox':
            return queryset.filter(data_nascimento__month=today.month+1)
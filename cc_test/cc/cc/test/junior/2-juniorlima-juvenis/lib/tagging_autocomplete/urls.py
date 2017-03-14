from django.conf.urls.defaults import *

urlpatterns = patterns('lib.tagging_autocomplete.views',
    url(r'^list$', 'list_tags', name='tagging_autocomplete-list'),
)

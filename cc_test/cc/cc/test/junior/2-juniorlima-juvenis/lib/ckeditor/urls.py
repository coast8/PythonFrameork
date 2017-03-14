from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^upload/', 'lib.ckeditor.views.upload', name='ckeditor_upload'),
    url(r'^browse/', 'lib.ckeditor.views.browse', name='ckeditor_browse'),
)

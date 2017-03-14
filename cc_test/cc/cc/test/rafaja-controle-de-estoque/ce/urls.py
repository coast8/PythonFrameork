from django.conf.urls.defaults import *
from estoque.views import teste, index
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ce/', include('ce.foo.urls')),
    (r'^teste/$', teste),
    
    (r'^index/$', direct_to_template, {'template':'estoque/index.html'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^teste/$', teste),
)

# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'
from django.conf.urls.defaults import *

urlpatterns = patterns('lib.tagging.views',
    url(r'^(?P<tag_name>.*?)/$', 'tag', name='tag'),
)
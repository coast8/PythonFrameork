# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'
"""
    # Remove espacos de pagina HTML
"""

from django.conf import settings
from django.utils.html import strip_spaces_between_tags

# spaceless middleware
class SpacelessMiddleware(object):
    force_spaceless = False
    def is_html(self, response):
        return 'text/html' in response['Content-Type']
    def processes(self, response):
        return not settings.DEBUG and response.status_code == 200
    def process_response(self, request, response):
        if self.is_html(response) and (self.processes(response) or self.force_spaceless):
            response.content = strip_spaces_between_tags(response.content.strip())
        return response

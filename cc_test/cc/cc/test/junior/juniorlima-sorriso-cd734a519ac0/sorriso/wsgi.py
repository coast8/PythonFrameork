"""
WSGI config for sorriso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/root/env/wellington/lib/python2.7/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sorriso.settings")
application = get_wsgi_application()

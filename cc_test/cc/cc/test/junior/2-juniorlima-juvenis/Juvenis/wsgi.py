import os
import sys
sys.path.append('/home/Juvenis')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Juvenis.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

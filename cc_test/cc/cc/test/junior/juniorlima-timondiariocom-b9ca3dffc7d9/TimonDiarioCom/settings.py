# coding=utf-8
# Django settings for TimonDiario project.

# -*- coding: utf-8 -*-
# Django settings for Juvenis project.
__author__ = 'Junior Rodrigues'

import os
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Junior Rodrigues', 'juniorrodrigues180@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'timondiario',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'passDigital02',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
TIME_ZONE = 'America/Fortaleza'
LANGUAGE_CODE = 'pt-BR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(PROJECT_DIR, '..', 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, '..', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ei!jn_oi0c0smy&n(ii6)f1f(w313y2%exenx-0%hna9ei6x*r'

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yawdadmin.middleware.PopupMiddleware',
    'lib.pagination.middleware.PaginationMiddleware',

)

ROOT_URLCONF = 'TimonDiarioCom.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'TimonDiarioCom.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'yawdadmin',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'lib.tagging',
    'lib.tagging_autocomplete',
    'lib.multiupload',
    'sorl.thumbnail',
    'lib.ckeditor',
    'lib.pagination',

    'igenius',
    'noticias',
    'core',
    'blogs',
    'times',
    'publicidades',
    'cliente',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
   from local_settings import *
except ImportError, e:
   pass

ADMIN_DISABLE_APP_INDEX = True
ADMIN_SITE_NAME = 'Timon Diário'
ADMIN_SITE_DESCRIPTION = 'Download, Tecnologia e Games (Assembled Agência i7)'

CKEDITOR_CONFIGS = {
    'junior': {
        'toolbar': [
            [
                'Undo', 'Redo',
                '-', 'Bold', 'Italic', 'Underline',
                '-', 'Link', 'Unlink',
                '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
                '-', 'Scayt',
                '-', 'BulletedList', 'NumberedList',
                '-', 'HorizontalRule', 'Blockquote' ,
                '-', 'Image',
                '-', 'Table',
                '-', 'Iframe'
                '-', 'Source',
            ],
        ],
        'height': 217,
        'width': 1100,
        'toolbarCanCollapse': False,
    },
}

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'arquivos')

THUMBNAIL_PREFIX = 'imagens/'
THUMBNAIL_BACKEND = 'core.seoimage.SEOThumbnailBackend'
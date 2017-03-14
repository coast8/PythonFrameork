# -*- coding: utf-8 -*-
# Django settings for Juvenis project.
__author__ = 'Junior Lima'
import os
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Junior Lima', 'webjuniorlima@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'juvenis',
        'USER': 'root',
        'PASSWORD': 'passDigital02',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['juvenis.com.br', 'www.juvenis.com.br']
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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '7t0orn6e^9jejd0!47hq=qe=ek3fl3*8g!lk&=+0p3+$mm*j!m'

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'core.context_processor.estaticos_context_processor'
)

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
    #'core.spaceless.SpacelessMiddleware', # Remove espacos em branco do HTML
)

ROOT_URLCONF = 'Juvenis.urls'

WSGI_APPLICATION = 'Juvenis.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.sitemaps',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yawdadmin',
    'django.contrib.admin',

    'lib.tagging',
    'lib.tagging_autocomplete',
    'lib.multiupload',
    'sorl.thumbnail',
    'lib.ckeditor',
    'lib.pagination',
    #'autofixture',

    'core',
    'blogs',
    'letras',
    'noticias',
    'locais',
    'publicidades',
    'campeonato',
    'administrativo',
    'shopping',
    'galeria',
    'event',
)


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
ADMIN_SITE_NAME = 'Juvenis'
ADMIN_SITE_DESCRIPTION = 'Notícias, Shows, Eventos, Letras, Música, Humor, Download, Estudos e Vídeos Gospel. Acesso Restrito'

CKEDITOR_CONFIGS = {
    'juniorlima': {
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
        'width': 756,
        'toolbarCanCollapse': False,
    },
}

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'arquivos')

THUMBNAIL_PREFIX = 'imagens/'
THUMBNAIL_BACKEND = 'core.seoimage.SEOThumbnailBackend'

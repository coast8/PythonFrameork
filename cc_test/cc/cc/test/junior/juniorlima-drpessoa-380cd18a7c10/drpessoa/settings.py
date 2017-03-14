# -*- coding: utf-8 -*-
__author__ = 'juniorlima'
"""
Django settings for drpessoa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tq-mhwh606f#6x7+q4z9*+d=avumhm=)m!&243&(yi*i)k6qwm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'easy_thumbnails',
    'ckeditor',
    'multiupload',
    'autofixture',

    'core',

    'assessoria',
    'galeria',
    'gabinete',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'drpessoa.urls'

WSGI_APPLICATION = 'drpessoa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drpessoa',
        'USER': 'root',
        'PASSWORD': 'passDigital02',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

# CK Editor
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'padrao': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
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
# Django Admin Bootstrap
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'core.context_processors.menusite',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


# Easy Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'home_noticia_300': {'size': (300, 225), 'crop': True},
        'timeline_410': {'size': (410, 160), 'crop': True},
        'home_noticia_1200': {'size': (1200, 400), 'crop': True},
        'home_noticia_850_640': {'size': (850, 400), 'crop': True},
        'home_noticia_900': {'size': (900, 0), 'crop': False},
        'imagem_galeria_240_160': {'size': (240, 160), 'crop': True},
    },
}

# Local settings
try:
   from local_settings import *
except ImportError, e:
   pass
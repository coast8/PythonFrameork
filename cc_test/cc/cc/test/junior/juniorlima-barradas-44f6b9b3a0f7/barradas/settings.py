# -*- coding: utf-8 -*-
__author__ = 'juniorlima'
"""
Django settings for barradas project.

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
SECRET_KEY = 'a&%za_$=8*37jg7a(lv-0e(-i23uihp4#^5igi5f8!kyn2vs(4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'easy_thumbnails',
    'ckeditor',

    'ads',
    'blogs',
    'portal',
)

# Template context processors
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'core.context_processors.menusite',
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

ROOT_URLCONF = 'barradas.urls'

WSGI_APPLICATION = 'barradas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'barradas',
        'USER': 'root',
        'PASSWORD': 'passDigital02',
        #'HOST': '',
        #'PORT': '',
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
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
MEDIA_URL = '/media/'
MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

# Local settings
try:
   from local_settings import *
except ImportError, e:
   pass

#EASY THUMBNAILS ALIASES
THUMBNAIL_ALIASES = {
    '': {
        'home_carrossel_540': {'size': (540, 355), 'crop': True},
        'home_noticias_350': {'size': (350, 230), 'crop': True},
        'home_videos_350_350': {'size': (350, 350), 'crop': True},
        'home_revista_350': {'size': (350, 0), 'crop': True},
        'home_noticias_800': {'size': (800, 0), 'crop': True},
        'home_noticias_320': {'size': (320, 0), 'crop': True},
        'home_noticias_800_530': {'size': (800, 530), 'crop': False},
        'blogueiro_141_141': {'size': (141, 141), 'crop': False},
        'home_noticias_800_nocrop': {'size': (800, 0), 'crop': False},
        'sidebar_95_80': {'size': (95, 80), 'crop': True},
    },
}

# CK EDITOR
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
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
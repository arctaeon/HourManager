"""
Django settings for wwustc project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'globalvalues'))
from GlobalSettings import *

# Disgusting looking code below that sets many variables to that of the global config
# Skip to next comment
#-----------------------------------------------------------------------------#
BASE_DIR = GLOBAL_BASE_DIR
SECRET_KEY = GLOBAL_SECRET_KEY
ALLOWED_HOSTS = GLOBAL_ALLOWED_HOSTS
INSTALLED_APPS = GLOBAL_INSTALLED_APPS
MIDDLEWARE = GLOBAL_MIDDLEWARE
LOGIN_URL = GLOBAL_LOGIN_URL
LOGIN_REDIRECT_URL = GLOBAL_LOGIN_REDIRECT_URL
AUTHENTICATED_BACKENDS = GLOBAL_AUTHENTICATED_BACKENDS
ROOT_URLCONF = GLOBAL_ROOT_URLCONF
WSGI_APPLICATION = GLOBAL_WSGI_APPLICATION
DATABASES = GLOBAL_DATABASES
AUTH_PASSWORD_VALIDATORS = GLOBAL_AUTH_PASSWORD_VALIDATORS
LANGUAGE_CODE = GLOBAL_LANGUAGE_CODE
TIME_ZONE = GLOBAL_TIME_ZONE
USE_I18N = GLOBAL_USE_I18N
USE_L10N = GLOBAL_USE_L10N
USE_TZ = GLOBAL_USE_TZ
STATIC_URL = GLOBAL_STATIC_URL
MEDIA_URL = GLOBAL_MEDIA_URL
SITE_ID = GLOBAL_SITE_ID
WIKI_ACCOUNT_HANDLING = GLOBAL_WIKI_ACCOUNT_HANDLING
WIKI_ACCOUNT_SIGNUP_ALLOWED = GLOBAL_WIKI_ACCOUNT_SIGNUP_ALLOWED
ADMIN_LIST = GLOBAL_ADMIN_LIST
NUM_USERS = GLOBAL_NUM_USERS
CREATING_SHIFTS = GLOBAL_CREATING_SHIFTS
USER_SHIFT_PLACE = GLOBAL_USER_SHIFT_PLACE
MOTD = GLOBAL_MOTD

#Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = GLOBAL_EMAIL_PORT
EMAIL_USE_TLS = GLOBAL_EMAIL_USE_TLS
EMAIL_HOST_USER = "stchours@gmail.com"
EMAIL_HOST_PASSWORD = "spr1ng20]8"
#-----------------------------------------------------------------------------#

# REPLACE WITH STATIC PATH TO FOLDER
# IMPORTANT (probably)
STATIC_ROOT = ''
MEDIA_ROOT = ''

SECURE_SSL_REDIRECT = False
DEBUG = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = True

ROOT_URLCONF = 'wwustc.local-dev-urls'

# Add custom apps here
INSTALLED_APPS += [
    'shiftmanager.apps.ShiftmanagerConfig',
]

# Add allowed hosts here
ALLOWED_HOSTS += [
    "localhost",
    "127.0.0.1",
]

# Add more middleware here
MIDDLEWARE += [
]

# Can override or add onto variables below

#-----------------------------------------------------------------------------#
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

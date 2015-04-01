"""
Django settings for seat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Production
SECRET_KEY = 'placeholder'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

#LDAP information
LDAP_HOST = 'ldap://ldap.patcave.info'
LDAP_ROOT_SEARCH_DN = 'dc=ldap,dc=patcave,dc=info'# we happen to log in as the root node when testing

# Applications
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seat',
    'dashboard',
    'login',
    'student'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'seat.custom_middleware.DashboardExceptionMiddleware'
)

ROOT_URLCONF = 'seat.urls'
WSGI_APPLICATION = 'seat.wsgi.application'

CSRF_COOKIE_HTTPONLY = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'prod':{
        'NAME'      : 'seat',
        'ENGINE'    : 'django.db.backends.mysql',
        'USER'      : 'capstone',
        'PASSWORD'  : '9324d1eb',
        'HOST'      : 'patcave.info',
        'PORT'      : '3306'
    }

}

# Template Settings
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Static Files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_URL = '/static/'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
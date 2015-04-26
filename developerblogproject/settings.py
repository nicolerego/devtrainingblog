"""
Django settings for developerblogproject project.
"""

import os
from os.path import join, dirname, abspath, basename, normpath

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c6i3u7dlkya!r2f3moskc#7&=o(5h7m!2kyyxrjixgh$ue)n8^'

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
    'django.contrib.sites',
    'django.contrib.comments',
    'blog',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'developerblogproject.urls'

WSGI_APPLICATION = 'developerblogproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static Files
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT= os.path.join(BASE_DIR)

MEDIA_URL = '/images/'

# Setting up logging for codepublish and design publish commands
__LOGGING_DIR_PREFIX =join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter' :{
            'format': '%(asctime)s - %(levelname)s %(message)s',
        },
    },
    'handlers': {
        'publishlogfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': join(__LOGGING_DIR_PREFIX, 'publishinfo.log'),
            'formatter': 'main_formatter',
        },
    },
    'loggers': {
        'django.blog': {
            'handlers': ['publishlogfile'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
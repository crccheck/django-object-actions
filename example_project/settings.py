# Django settings for example_project project.
import os

import dj_database_url


def project_dir(*paths):
    base = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(base, *paths)


DEBUG = True

DATABASES = {'default': dj_database_url.config(default='sqlite:///' +
    project_dir('example_project.db'))}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_L10N = False

USE_TZ = False

STATIC_URL = '/static/'

SECRET_KEY = 'lolimasekrit'

ROOT_URLCONF = 'example_project.urls'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'example_project.polls',

    # my app
    'django_object_actions',

    # dev helpers
    'django_extensions',
)


# STFU, Django 1.7
# To be deleted once Django 1.8 testing begins
SILENCED_SYSTEM_CHECKS = [
    '1_7.W001',
]

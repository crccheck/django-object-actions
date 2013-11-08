# Django settings for example_project project.
import os

import dj_database_url


def project_dir(*paths):
    base = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(base, *paths)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='sqlite:///' +
    project_dir('example_project.sqlite'))}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'lolimasekrit'

ROOT_URLCONF = 'example_project.urls'


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
    # testing
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

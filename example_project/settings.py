# Django settings for example_project project.
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent

DEBUG = True

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'example_project.db'}"
    )
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

TIME_ZONE = "America/Chicago"
LANGUAGE_CODE = "en-us"
USE_TZ = False

STATIC_URL = "/static/"

SECRET_KEY = "lolimasekrit"

ROOT_URLCONF = "example_project.urls"

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)


INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "example_project.polls",
    # my app
    "django_object_actions",
    # dev helpers
    "django_extensions",
)


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
